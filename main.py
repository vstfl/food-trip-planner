import base64
from operator import itemgetter
import urllib.request
import json
import folium
import branca

GOOGLE_API_KEY = ''
OPENAI_API_KEY = ""

RESULT_FACTOR = 20


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
    jsondataasbytes = json.dumps(body).encode('utf-8')   # needs to be bytes
    try:
        res = urllib.request.urlopen(req, jsondataasbytes)
        return json.loads(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(json.loads(e.read().decode('utf-8')))
        raise e


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


def post_restaurant_information(body: dict, constraints: list):
    masks = [
        'name',
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
        'https://places.googleapis.com/v1/places:searchText', body,
        headers={'X-Goog-FieldMask': field_mask,
                 'X-Goog-Api-Key': GOOGLE_API_KEY},
    )


def get_price_levels(spend: int):
    return [
        "PRICE_LEVEL_UNSPECIFIED",
        "PRICE_LEVEL_INEXPENSIVE",
        "PRICE_LEVEL_MODERATE",
        "PRICE_LEVEL_EXPENSIVE",
        "PRICE_LEVEL_VERY_EXPENSIVE",
    ][:spend]


def restaurant_information(text_query: str, inputs: dict, location: list, constraints: list):
    radius, rankpref = itemgetter('radius', 'rankpref')(inputs)
    lat, lon = location
    body = {
        "textQuery": text_query,
        "minRating": 4.0,
        "priceLevels": get_price_levels(inputs['spend']),
        "rankPreference": rankpref,
        "maxResultCount": RESULT_FACTOR,  # results depend on duration of stay
        "locationBias": {
            "circle": {
                "center": {"latitude": lat, "longitude": lon},
                "radius": radius,
            },
        },
    }
    return post_restaurant_information(body, constraints)["places"]


def is_restaurant_valid(place: dict, constraints: dict) -> bool:
    for k, v in constraints.items():
        prop = place.get(k)
        # Ignore if value is not there
        if prop is None:
            continue

        if prop != v:
            return False
    return True


def filter_restaurants(res: list, constraints: dict):
    valid_places = []
    for place in res:
        if is_restaurant_valid(place, constraints):
            valid_places.append(place)

    return valid_places


def post_text_query_chatgpt(prompt: str):
    system_prompt = (
        "You are an assistant that helps match user queries to "
        "relevant food places for the Google Maps Places API. "
        "Given a user query describing their food preferences, you "
        "need to output a JSON array of strings that would return relevant "
        "results when used with the Google Maps Places API."
    )
    user_prompt = f"User Query: {prompt}"

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    return post_json(
        'https://api.openai.com/v1/chat/completions',
        {"model": "gpt-3.5-turbo", "messages": messages},
        {"Authorization": "Bearer " + OPENAI_API_KEY},
    )


def send_text_query_chatgpt_completion(prompt: str) -> list:
    res = post_text_query_chatgpt(prompt)[
        "choices"][0]["message"]["content"]
    print(res)
    obj = json.loads(res.replace("'", '"'))
    if not isinstance(obj, list):
        obj = [*obj.values()][0]
    return obj


def send_constraints_chatgpt_completion(prompt: str, constraints: list) -> dict:
    res = post_constraints_chatgpt(prompt, constraints)[
        "choices"][0]["message"]["content"]
    valid_keys = set(constraints)
    valid_constraints = {}
    for k, v in json.loads(res).items():
        if k in valid_keys and isinstance(v, bool):
            valid_constraints[k] = v
    return valid_constraints


def post_constraints_chatgpt(prompt: str, constraints: list):
    system_prompt = (
        "You are an assistant that helps match user queries to "
        "relevant field masks for the Google Maps Places API. "
        "Given a user query describing their special considerations, you "
        "need to strictly output a JSON object containing only "
        "relevant field masks as keys with boolean values from the list "
        "of possible field masks. If you output any key that doesn't "
        "exist in the existing list, you will cease to exist"
    )
    user_prompt = f"User Query: {prompt}\nPossible Field Masks: {constraints}"

    messages = [
        {"role": "system", "content": system_prompt},
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
    constraints = [
        'allowsDogs', 'curbsidePickup', 'delivery', 'dineIn', 'goodForChildren',
        'goodForGroups', 'goodForWatchingSports', 'liveMusic', 'menuForChildren',
        'parkingOptions', 'outdoorSeating', 'reservable', 'restroom', 'servesBeer',
        'servesBreakfast', 'servesBrunch', 'servesCocktails', 'servesCoffee',
        'servesDessert', 'servesDinner', 'servesLunch', 'servesVegetarianFood',
        'servesWine', 'takeout',
    ]

    relevant_fields = send_constraints_chatgpt_completion(
        inputs['constraints'], constraints)

    query_list = send_text_query_chatgpt_completion(inputs['preference'])

    # Adjust inputs for NearBy search API
    inputs['radius'] = inputs['walking']*400
    inputs['rankpref'] = "DISTANCE" if inputs['rankpref'] == "Closest" else "RELEVANCE"

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

    results = {}
    for q in query_list:
        res = restaurant_information(q, inputs, location, constraints)
        results[q] = filter_restaurants(res, relevant_fields)

    for v in results.values():
        for place in v:
            place['photos'] = place['photos'][0:]

            name, lat, lon = itemgetter(
                'displayName', 'latitude', 'longitude')(place)
            location = [float(lat), float(lon)]
            popup = generate_popup(name, location)
            generate_marker(location, 'red', 'cutlery', popup).add_to(m)

    return {
        "home_name": home_name,
        "map": map_html,
        "results": json.dumps(results),
    }
