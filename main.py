import base64
from operator import itemgetter
import urllib.request
import json
import folium
import branca

GOOGLE_API_KEY = ''
OPENAI_API_KEY = ""


def get_photo_src(photo_name: str):
    blob = urllib.request.urlopen(
        f'https://places.googleapis.com/v1/{photo_name}/media?maxHeightPx=400&maxWidthPx=400&key={GOOGLE_API_KEY}').read()
    b = base64.b64encode(blob).decode("utf-8")
    return f"data:image/png;base64,{b}"


def post_json(url: str, body: object, headers: dict = {}):
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    for k, v in headers.items():
        req.add_header(k, v)
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    res = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(res.read().decode('utf-8'))


def post_hotel_location(place: str, city: str):
    return post_json(
        'https://places.googleapis.com/v1/places:searchText',
        {"textQuery": " ".join((place, city))},
        headers={
            'X-Goog-FieldMask': 'places.displayName,places.location',
            'X-Goog-Api-Key': GOOGLE_API_KEY,
        }
    )


def hotel_coordinates(place: str, city: str):
    places = post_hotel_location(place, city)["places"][0]
    name, location = places["displayName"]["text"], places["location"]
    return name, location["latitude"], location["longitude"]
    

def post_restaurant_information(body: dict):
    masks = [
        'displayName',
        'location',
        'rating',
        'priceLevel',
        'websiteUri',
        "formattedAddress",
        "userRatingCount",
        "photos.name",
    ] + constraints
    field_mask = ",".join('places.' + i for i in masks)
    return post_json(
        'https://places.googleapis.com/v1/places:searchNearby', body,
        headers={'X-Goog-FieldMask': field_mask,
                 'X-Goog-Api-Key': GOOGLE_API_KEY},
    )


def restaurant_information(input: dict, location: list):
    types, days, radius, rankpref = itemgetter(
        'types', 'days', 'radius', 'rankpref')(input)
    lat, lon = location
    body = {
        "includedTypes": types,
        "excludedTypes": ['bar'],
        "rankPreference": rankpref,
        "maxResultCount": 15*days,  # results depend on duration of stay
        "locationRestriction": {
            "circle": {
                "center": {"latitude": lat, "longitude": lon},
                "radius": radius
            }
        }
    }
    res = post_restaurant_information(body)["places"]
    price_levels = {
        "PRICE_LEVEL_UNSPECIFIED": -1,
        "PRICE_LEVEL_FREE": 0,
        "PRICE_LEVEL_INEXPENSIVE": 1,
        "PRICE_LEVEL_MODERATE": 2,
        "PRICE_LEVEL_EXPENSIVE": 3,
        "PRICE_LEVEL_VERY_EXPENSIVE": 4,
        None: 6,  # Exclude places with no price level
    }

    valid_places = []

    for place in res:
        if (price_levels[place.get('priceLevel')] <= inputs['spend']) and (place.get('rating', 0) >= 4.0):
            valid_places.append(place)

    return valid_places


def post_placetype_chatgpt(prompt: str, place_types: list):
    system_prompt = (
        "You are an assistant that helps match user queries to "
        "relevant place types for the Google Maps Places API. "
        "Given a user query describing their food preferences, you "
        "need to strictly output a JSON array containing only "
        "relevant place types from the possible place types. If you "
        "output anything that doesn't exist in the possible place "
        "types, you will cease to exist"
    )
    user_prompt = f"User Query: {prompt}\nPossible Place Types: {place_types}"

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    return post_json(
        'https://api.openai.com/v1/chat/completions',
        {"model": "gpt-3.5-turbo", "messages": messages},
        {"Authorization": "Bearer " + OPENAI_API_KEY},
    )


def send_placetype_chatgpt_completion(prompt: str, place_types: list) -> list:
    res = post_placetype_chatgpt(prompt, place_types)[
        "choices"][0]["message"]["content"]
    # Make sure that the place types are valid
    return list(set(json.loads(res)).intersection(place_types))


def send_constraints_chatgpt_completion(prompt: str, constraints: list) -> str:
    res = post_constraints_chatgpt(prompt, constraints)[
        "choices"][0]["message"]["content"]
    # Make sure that the place types are valid
    return list(set(json.loads(res)).intersection(constraints))


def post_constraints_chatgpt(prompt: str, constraints: list):
    # TODO: Change this system prompt
    system_prompt = (
        "You are an assistant that helps match user queries to "
        "relevant field masks for the Google Maps Places API. "
        "Given a user query describing their special considerations, you "
        "need to strictly output a JSON array containing only "
        "relevant field masks from the list of possible field masks. If you "
        "output anything that doesn't exist in the existing list, "
        "you will cease to exist"
    )
    user_prompt = f"User Query: {prompt}\nPossible Field Masks: {constraints}"

    messages = [
        {"role": "system", "content": system_prompt},
        # Add more messages as needed
        {"role": "user", "content": user_prompt},
    ]
    return post_json(
        'https://api.openai.com/v1/chat/completions',
        {"model": "gpt-3.5-turbo", "messages": messages},
        {"Authorization": "Bearer " + OPENAI_API_KEY},
    )


def generate_marker(coords: list, color: str, icon: str, pop: folium.Popup):
    # Icons choices: https://getbootstrap.com/docs/3.3/components/
    return folium.Marker(coords, pop, icon=folium.Icon(color=color, icon=icon))


def generate_popup(name: str, coords: list):
    # TODO: Modify parameters and things to be displayed
    html = f'''
    <p style="text-align:center">{name}</p>
    <p align="center">
        <iframe width="350" height="250" style="border:0" loading="lazy" allowfullscreen
            src="https://www.google.com/maps/embed/v1/streetview?location={coords[0]}%2C{coords[1]}&key=AIzaSyBejfCQlJmEkQPRMHffCLLp0YfyZN-Z6FQ">
        </iframe>
    </p>
    '''
    html = branca.element.IFrame(html=html, width="400", height="350")
    popup = folium.Popup(html, max_width=400)
    return popup


def main(inputs):
    debug = ''

    place_types = [
        'american_restaurant', 'bakery', 'bar', 'barbecue_restaurant',
        'brazilian_restaurant', 'breakfast_restaurant', 'brunch_restaurant',
        'cafe', 'chinese_restaurant', 'coffee_shop', 'fast_food_restaurant',
        'french_restaurant', 'greek_restaurant', 'hamburger_restaurant',
        'ice_cream_shop', 'indian_restaurant', 'indonesian_restaurant',
        'italian_restaurant', 'japanese_restaurant', 'korean_restaurant',
        'lebanese_restaurant', 'meal_delivery', 'meal_takeaway',
        'mediterranean_restaurant', 'mexican_restaurant',
        'middle_eastern_restaurant', 'pizza_restaurant', 'ramen_restaurant',
        'restaurant', 'sandwich_shop', 'seafood_restaurant',
        'spanish_restaurant', 'steak_house', 'sushi_restaurant',
        'thai_restaurant', 'turkish_restaurant', 'vegan_restaurant',
        'vegetarian_restaurant', 'vietnamese_restaurant',
    ]

    constraints = [
        'allowsDogs', 'curbsidePickup', 'delivery', 'dineIn', 'goodForChildren', 
        'goodForGroups', 'goodForWatchingSports', 'liveMusic', 'menuForChildren', 
        'parkingOptions', 'outdoorSeating', 'reservable', 'restroom', 'servesBeer', 
        'servesBreakfast', 'servesBrunch', 'servesCocktails', 'servesCoffee', 
        'servesDesserts', 'servesDinner', 'servesLunch', 'servesVegetarianFood', 
        'servesWine', 'takeout'
    ]

    relevant_fields = send_constraints_chatgpt_completion(
        inputs['constraints'], constraints)
    
    relevant_types = send_placetype_chatgpt_completion(
        inputs['preference'], place_types)
    inputs['types'] = relevant_types

    # Adjust inputs for NearBy search API
    inputs['radius'] = inputs['walking']*400
    inputs['rankpref'] = "DISTANCE" if inputs['rankpref'] == "Closest" else "POPULARITY"

    # Home input
    home_name, lat, lon = hotel_coordinates(inputs['hotel'], inputs['city'])
    location = [float(lat), float(lon)]

    # Generate Folium map
    m = folium.Map(location=location, zoom_start=15, tiles="OpenStreetMap")

    # Place nodes

    # Home node
    home_popup = generate_popup(home_name, location)
    generate_marker(location, 'blue', 'home', home_popup).add_to(m)

    # Export folium map as HTML string
    map_html = m._repr_html_()

    res = restaurant_information(inputs, location)

    return {
        "home_name": home_name,
        "map": map_html,
        "debug": debug,
        "place_types": relevant_types,
    }
