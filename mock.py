import json


def main(inputs):
    s = """
    {
        "home_name": "Fantasyland Hotel",
        "results": {
            "1": {
                "Breakfast": {
                    "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI",
                    "formattedAddress": "2512 Guardian Rd NW, Edmonton, AB T5T 1K8, Canada",
                    "location": {
                        "latitude": 53.5095095,
                        "longitude": -113.674498
                    },
                    "rating": 4.1,
                    "websiteUri": "https://www.originaljoes.ca/en/locations/ab/edmonton/2512-guardian-road-nw",
                    "priceLevel": "PRICE_LEVEL_MODERATE",
                    "userRatingCount": 746,
                    "displayName": {
                        "text": "Original Joe's",
                        "languageCode": "en"
                    },
                    "takeout": true,
                    "delivery": true,
                    "dineIn": true,
                    "curbsidePickup": false,
                    "reservable": true,
                    "servesBreakfast": true,
                    "servesLunch": true,
                    "servesDinner": true,
                    "servesBeer": true,
                    "servesWine": true,
                    "servesBrunch": true,
                    "servesVegetarianFood": true,
                    "photos": [
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjyAcO14wvEK-gCQWG97TErc0TeAXH_CSPEPCEkru1e3vcowrDxNaAhhic9Ytf8Teh4NLoDCDjmsgtnwH327r4I2f7lviw-ZFGQ5CEosiLm6xfpV00OfdieF4hOfY1w3Em199vZqUZi0K_lDQ124tqwzO66jn3gWd5D"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjnTXpVyxQlKvDbQGr__eQAv6VamgMfMBDuyCNg_7ZkSxgwgCOPRvGX3MSu2Q8b6hnd75ZDI99WXsyhKuMD8x0ssOCyWe-pWDE77li-HKxFzRbYxmpjNR_43Lr9aO1dX-72qkT75OhbVuTO-dJ9Sht8gsrbof8iEoxq"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjk9_TirYN9Wtb4UttGKANvFlM7VvEg2C-yH8rgV8-pSG6kTOY1Z8hKZWz6gmemxb5mDWDrRT12vFU88pwlgEjhYf8SZXyxULPWaiJqLvkiq9Zb4IDPxPp2k7yzogbZBqrQGbNgRGOWHJf8PDEe1PqX-qPWcIYRzCCr"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhEY9QaydYRsNOn9lpLNmXiehDfWGOlbvtyBNQiRuApWXny-NHblCb8Uo1iVEqOkTEU-0jc8477gamTld-9bG20LLZF7Cvhnfz_bmGvlBGQEkHbMWPInZ9oK9q59JGimDWj2y3Em00i6A8ELAdBw6KNsU0MGVi9-nK8"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjpUG5BhkaUd0EdwqjsUl44Dn78z6xURip50yFXIGhZLRt9E6e-i0ffzI0KVryd8fcn62kdK1fchrNVAfxT1a3ln7SCc7eRHEZZwIAnM2h8SypRHdKb-wCHJCHRbGlJCpiOa11wUnahqrE2usqL1l80FL1nnOvJA_3q"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFh-0kqrdC9dZaVbhTyH8840TJiPhnbp0bUkmYnCMw6AbDR4z1aYtpEVk9G8P-2Ae3LDCZT2wtbLcydOiSohYJhOdkRDViy_l91FgUTdFgQBviuOdJvxRPndG2yIYtodTxVUuAq__NIoQmdmkWSBwksfjaww3bVltJla"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjDk9a-TNORZwv3aHDvScKbmeM2LYCvUh14pwjKHdjkFVKxN3NXNkPlLWjXWMssutn8UmE3-DFmoKgGJLw94aFRZjdWfuGizj9a_0rBbSHJ299ZhcdsLtg0GfiYF935B2WmUOEGTQ80Z1LUB_ORXPNTTo6jTXkoaA-e"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjHZhmHmxYC-p9Cb_dxha_O2aoioDKsBl5ykGMAbtRpk1LIOVAX7IRO03jDw2_pEqfAtShnvihPkueQIvs7flppV0VBr1vGEIqHAblvFUFkK7MiQ712iVMHcNLE-8dsLiqeuCIIIiI85M2_jOwrT2qeTXHz5llSJQqY"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhnOkaTElrIJYDaZoV46TrzwG1b_aY-AkxP8JPec5s0CQ-hxUDusz6OyiXytnLBQHoFdz78msFiKJZGOJMMLtC04mHRtWzW4CKZh_iLSfoOXcuKKqXZ9qiMfQbNyqlOxEeIqMsCj9RzCB9aRho_tDL6gQR0V-t4c0tZ"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhJLlYL8mIGZQkZxMre7cEo4qWpLnblnI6NXtRR3-E_KSe4U2kSk-lweilSmq59kLIe9MEaiwRb_obXmrYbITHwC7LACVVFsDbyjK84vXsWpUEY5Xth5FOHFzecC7TSg6hHMumOPe1ppY9n3WRSJCAgW1_defGmt6oM"
                        }
                    ],
                    "outdoorSeating": true,
                    "liveMusic": false,
                    "menuForChildren": true,
                    "servesCocktails": true,
                    "servesDessert": true,
                    "servesCoffee": true,
                    "goodForChildren": false,
                    "restroom": true,
                    "goodForGroups": true,
                    "goodForWatchingSports": true,
                    "parkingOptions": {
                        "freeParkingLot": true
                    }
                },
                "Lunch": {
                    "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI",
                    "formattedAddress": "2512 Guardian Rd NW, Edmonton, AB T5T 1K8, Canada",
                    "location": {
                        "latitude": 53.5095095,
                        "longitude": -113.674498
                    },
                    "rating": 4.1,
                    "websiteUri": "https://www.originaljoes.ca/en/locations/ab/edmonton/2512-guardian-road-nw",
                    "priceLevel": "PRICE_LEVEL_MODERATE",
                    "userRatingCount": 746,
                    "displayName": {
                        "text": "Original Joe's",
                        "languageCode": "en"
                    },
                    "takeout": true,
                    "delivery": true,
                    "dineIn": true,
                    "curbsidePickup": false,
                    "reservable": true,
                    "servesBreakfast": true,
                    "servesLunch": true,
                    "servesDinner": true,
                    "servesBeer": true,
                    "servesWine": true,
                    "servesBrunch": true,
                    "servesVegetarianFood": true,
                    "photos": [
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjyAcO14wvEK-gCQWG97TErc0TeAXH_CSPEPCEkru1e3vcowrDxNaAhhic9Ytf8Teh4NLoDCDjmsgtnwH327r4I2f7lviw-ZFGQ5CEosiLm6xfpV00OfdieF4hOfY1w3Em199vZqUZi0K_lDQ124tqwzO66jn3gWd5D"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjnTXpVyxQlKvDbQGr__eQAv6VamgMfMBDuyCNg_7ZkSxgwgCOPRvGX3MSu2Q8b6hnd75ZDI99WXsyhKuMD8x0ssOCyWe-pWDE77li-HKxFzRbYxmpjNR_43Lr9aO1dX-72qkT75OhbVuTO-dJ9Sht8gsrbof8iEoxq"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjk9_TirYN9Wtb4UttGKANvFlM7VvEg2C-yH8rgV8-pSG6kTOY1Z8hKZWz6gmemxb5mDWDrRT12vFU88pwlgEjhYf8SZXyxULPWaiJqLvkiq9Zb4IDPxPp2k7yzogbZBqrQGbNgRGOWHJf8PDEe1PqX-qPWcIYRzCCr"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhEY9QaydYRsNOn9lpLNmXiehDfWGOlbvtyBNQiRuApWXny-NHblCb8Uo1iVEqOkTEU-0jc8477gamTld-9bG20LLZF7Cvhnfz_bmGvlBGQEkHbMWPInZ9oK9q59JGimDWj2y3Em00i6A8ELAdBw6KNsU0MGVi9-nK8"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjpUG5BhkaUd0EdwqjsUl44Dn78z6xURip50yFXIGhZLRt9E6e-i0ffzI0KVryd8fcn62kdK1fchrNVAfxT1a3ln7SCc7eRHEZZwIAnM2h8SypRHdKb-wCHJCHRbGlJCpiOa11wUnahqrE2usqL1l80FL1nnOvJA_3q"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFh-0kqrdC9dZaVbhTyH8840TJiPhnbp0bUkmYnCMw6AbDR4z1aYtpEVk9G8P-2Ae3LDCZT2wtbLcydOiSohYJhOdkRDViy_l91FgUTdFgQBviuOdJvxRPndG2yIYtodTxVUuAq__NIoQmdmkWSBwksfjaww3bVltJla"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjDk9a-TNORZwv3aHDvScKbmeM2LYCvUh14pwjKHdjkFVKxN3NXNkPlLWjXWMssutn8UmE3-DFmoKgGJLw94aFRZjdWfuGizj9a_0rBbSHJ299ZhcdsLtg0GfiYF935B2WmUOEGTQ80Z1LUB_ORXPNTTo6jTXkoaA-e"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjHZhmHmxYC-p9Cb_dxha_O2aoioDKsBl5ykGMAbtRpk1LIOVAX7IRO03jDw2_pEqfAtShnvihPkueQIvs7flppV0VBr1vGEIqHAblvFUFkK7MiQ712iVMHcNLE-8dsLiqeuCIIIiI85M2_jOwrT2qeTXHz5llSJQqY"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhnOkaTElrIJYDaZoV46TrzwG1b_aY-AkxP8JPec5s0CQ-hxUDusz6OyiXytnLBQHoFdz78msFiKJZGOJMMLtC04mHRtWzW4CKZh_iLSfoOXcuKKqXZ9qiMfQbNyqlOxEeIqMsCj9RzCB9aRho_tDL6gQR0V-t4c0tZ"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhJLlYL8mIGZQkZxMre7cEo4qWpLnblnI6NXtRR3-E_KSe4U2kSk-lweilSmq59kLIe9MEaiwRb_obXmrYbITHwC7LACVVFsDbyjK84vXsWpUEY5Xth5FOHFzecC7TSg6hHMumOPe1ppY9n3WRSJCAgW1_defGmt6oM"
                        }
                    ],
                    "outdoorSeating": true,
                    "liveMusic": false,
                    "menuForChildren": true,
                    "servesCocktails": true,
                    "servesDessert": true,
                    "servesCoffee": true,
                    "goodForChildren": false,
                    "restroom": true,
                    "goodForGroups": true,
                    "goodForWatchingSports": true,
                    "parkingOptions": {
                        "freeParkingLot": true
                    }
                }
            },
            "2": {
                "Breakfast": {
                    "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI",
                    "formattedAddress": "2512 Guardian Rd NW, Edmonton, AB T5T 1K8, Canada",
                    "location": {
                        "latitude": 53.5095095,
                        "longitude": -113.674498
                    },
                    "rating": 4.1,
                    "websiteUri": "https://www.originaljoes.ca/en/locations/ab/edmonton/2512-guardian-road-nw",
                    "priceLevel": "PRICE_LEVEL_MODERATE",
                    "userRatingCount": 746,
                    "displayName": {
                        "text": "Original Joe's",
                        "languageCode": "en"
                    },
                    "takeout": true,
                    "delivery": true,
                    "dineIn": true,
                    "curbsidePickup": false,
                    "reservable": true,
                    "servesBreakfast": true,
                    "servesLunch": true,
                    "servesDinner": true,
                    "servesBeer": true,
                    "servesWine": true,
                    "servesBrunch": true,
                    "servesVegetarianFood": true,
                    "photos": [
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFi4qAvUZZAQ2td2-oQMGL1lZs1gC8qVno4dQ3jFnEVJZxDoEqW6DLYZmj6wRg6alz4S-TlfTsRNRZo6u9n0P1-uNCWMsUzEAkaesyLAQ_VsSbY5mM55sltkGiF_AaPqmQFrmd8aKuweVzpxcF0q3OKzCo3SFkBMq4_a"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFi25x4ApXPQjgj6W7fQKIq2TPHXBkaLNaTkdwCRptZSya3v2iEi8IabfOUwh_ETc5soyrwObzZW8M66XUrKJzYtyktab2OMDWyg-2e4SrGtKdwxE-FP_B9q5XJI4IwRIoooksjp90Chhk73gdD4HYoezts2cM02gex3"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFiAIFS3h-sr6qJPl_X2rEK7CeE8qCHU6ITxMKSbW_B5ecGuZGRF8F88PJ8kwKoPmYBJVJTlOxzHS1vuncF6AE9PvzUD5l7Rf5vNiR60iWvuYO_E1_krwKAD3oNCSHETOcoJrJn666kL49gWIHc1OF2xxwTBQbv8mtZn"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFid9Hchj4D9SioPPmRCIF4F2UZxZDsw5A8D71O1d-heN9l5jBVPUxKiYjTuAdUl3F_RvX-1pC2LmJWmYuSiMq1ZrgqESSoKDkil-FYE3zbA7UFjUSA8PX-wJVjAy5rj7qFqPIRDqbiqp-mJ8e1VtyI1Btlh2oCW-119"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFgeslPrnzQCjXxN-AXQsOqttiSRn19hYPIHE_bOgBVj7ozC-NYmMHD8Fw6VvK6CHeueI-gtGl2WX2Lv-4RCVdhlX8r_-xXdmUglxfdGORuZmtcxSxWLxLzDKwhNuKlQ_R6TMzSKZlX8V6K66xQOWVsFwFtR32UpWu0k"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjisbUnMXvlWOuOINypangHWeNsCvbWrDpMEOxjSTLKvIxl4zE9JjOPLCqCis1waLpc11ZgMeOCQSEX6OJ4pKaYArymGRCf3aoSgziXBZFe-BhtspAcohFxS6p5Duq9n-vIGlGE33sb8gxtjj6mmmN3YsjGUmEX-_WR"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhe2ve9jfOOkcHsQetCcZmdC9OBAiNwPoGIWdyEsAXus9YQvK1qHzlNVzSOlBwrk5C7UYiCQXhHUX8dyJx2pFaqoq1IVjWjthOP8INrIVOF13Hy2BqfeyZR-ZQndld1ljDJhYOIuUjqokGonTf0XFyecwC7zvc1zsRU"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFgIOOfU68au5p7H69H3UAkjeYW4K33STC0FTqpskA1zTXfqRezyFQ6TlGX4B_4TP1zq6EOqMdnraYZcjzu8Qb6zmIIErxuGjUw4Zo2fDM0cjy4k9w8mu6cLNPvqBPt00u1_EiscgMZldPWnBx7gifODYhM_lxClbRoN"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFgd1qk0ZNHT7or3At2naCGrUDJywvlQcRAJfS7-Y6pzfXrZ1EeL8UyqVlVFiFAKcIr43Af-92DA2f87VuAeiUlYshC-CLCIOSmgHZfhAUrxq8N39dbhHPrVB3MTKL2WsU-p8Rlt9oDn3RIJtmuW0jVzJvYVeEx5Z27H"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjPNm-aeErIZMd2jWKn1O_YGsFzmjnrn6TQCG66fq5IpQ_AneF7NljhQZMpBooPxY5_blOnGkc7PcjMNN8SFJr8zn8NJcyMPJ7Z2ZT9IRXktHMz1QUDsouHQDZJ5PY4xtSLXBo1iSCraH3dV4rFVnC3l_Y8T5RyGVBc"
                        }
                    ],
                    "outdoorSeating": true,
                    "liveMusic": false,
                    "menuForChildren": true,
                    "servesCocktails": true,
                    "servesDessert": true,
                    "servesCoffee": true,
                    "goodForChildren": false,
                    "restroom": true,
                    "goodForGroups": true,
                    "goodForWatchingSports": true,
                    "parkingOptions": {
                        "freeParkingLot": true
                    }
                },
                "Lunch": {
                    "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI",
                    "formattedAddress": "2512 Guardian Rd NW, Edmonton, AB T5T 1K8, Canada",
                    "location": {
                        "latitude": 53.5095095,
                        "longitude": -113.674498
                    },
                    "rating": 4.1,
                    "websiteUri": "https://www.originaljoes.ca/en/locations/ab/edmonton/2512-guardian-road-nw",
                    "priceLevel": "PRICE_LEVEL_MODERATE",
                    "userRatingCount": 746,
                    "displayName": {
                        "text": "Original Joe's",
                        "languageCode": "en"
                    },
                    "takeout": true,
                    "delivery": true,
                    "dineIn": true,
                    "curbsidePickup": false,
                    "reservable": true,
                    "servesBreakfast": true,
                    "servesLunch": true,
                    "servesDinner": true,
                    "servesBeer": true,
                    "servesWine": true,
                    "servesBrunch": true,
                    "servesVegetarianFood": true,
                    "photos": [
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFi4qAvUZZAQ2td2-oQMGL1lZs1gC8qVno4dQ3jFnEVJZxDoEqW6DLYZmj6wRg6alz4S-TlfTsRNRZo6u9n0P1-uNCWMsUzEAkaesyLAQ_VsSbY5mM55sltkGiF_AaPqmQFrmd8aKuweVzpxcF0q3OKzCo3SFkBMq4_a"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFi25x4ApXPQjgj6W7fQKIq2TPHXBkaLNaTkdwCRptZSya3v2iEi8IabfOUwh_ETc5soyrwObzZW8M66XUrKJzYtyktab2OMDWyg-2e4SrGtKdwxE-FP_B9q5XJI4IwRIoooksjp90Chhk73gdD4HYoezts2cM02gex3"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFiAIFS3h-sr6qJPl_X2rEK7CeE8qCHU6ITxMKSbW_B5ecGuZGRF8F88PJ8kwKoPmYBJVJTlOxzHS1vuncF6AE9PvzUD5l7Rf5vNiR60iWvuYO_E1_krwKAD3oNCSHETOcoJrJn666kL49gWIHc1OF2xxwTBQbv8mtZn"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFid9Hchj4D9SioPPmRCIF4F2UZxZDsw5A8D71O1d-heN9l5jBVPUxKiYjTuAdUl3F_RvX-1pC2LmJWmYuSiMq1ZrgqESSoKDkil-FYE3zbA7UFjUSA8PX-wJVjAy5rj7qFqPIRDqbiqp-mJ8e1VtyI1Btlh2oCW-119"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFgeslPrnzQCjXxN-AXQsOqttiSRn19hYPIHE_bOgBVj7ozC-NYmMHD8Fw6VvK6CHeueI-gtGl2WX2Lv-4RCVdhlX8r_-xXdmUglxfdGORuZmtcxSxWLxLzDKwhNuKlQ_R6TMzSKZlX8V6K66xQOWVsFwFtR32UpWu0k"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjisbUnMXvlWOuOINypangHWeNsCvbWrDpMEOxjSTLKvIxl4zE9JjOPLCqCis1waLpc11ZgMeOCQSEX6OJ4pKaYArymGRCf3aoSgziXBZFe-BhtspAcohFxS6p5Duq9n-vIGlGE33sb8gxtjj6mmmN3YsjGUmEX-_WR"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhe2ve9jfOOkcHsQetCcZmdC9OBAiNwPoGIWdyEsAXus9YQvK1qHzlNVzSOlBwrk5C7UYiCQXhHUX8dyJx2pFaqoq1IVjWjthOP8INrIVOF13Hy2BqfeyZR-ZQndld1ljDJhYOIuUjqokGonTf0XFyecwC7zvc1zsRU"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFgIOOfU68au5p7H69H3UAkjeYW4K33STC0FTqpskA1zTXfqRezyFQ6TlGX4B_4TP1zq6EOqMdnraYZcjzu8Qb6zmIIErxuGjUw4Zo2fDM0cjy4k9w8mu6cLNPvqBPt00u1_EiscgMZldPWnBx7gifODYhM_lxClbRoN"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFgd1qk0ZNHT7or3At2naCGrUDJywvlQcRAJfS7-Y6pzfXrZ1EeL8UyqVlVFiFAKcIr43Af-92DA2f87VuAeiUlYshC-CLCIOSmgHZfhAUrxq8N39dbhHPrVB3MTKL2WsU-p8Rlt9oDn3RIJtmuW0jVzJvYVeEx5Z27H"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjPNm-aeErIZMd2jWKn1O_YGsFzmjnrn6TQCG66fq5IpQ_AneF7NljhQZMpBooPxY5_blOnGkc7PcjMNN8SFJr8zn8NJcyMPJ7Z2ZT9IRXktHMz1QUDsouHQDZJ5PY4xtSLXBo1iSCraH3dV4rFVnC3l_Y8T5RyGVBc"
                        }
                    ],
                    "outdoorSeating": true,
                    "liveMusic": false,
                    "menuForChildren": true,
                    "servesCocktails": true,
                    "servesDessert": true,
                    "servesCoffee": true,
                    "goodForChildren": false,
                    "restroom": true,
                    "goodForGroups": true,
                    "goodForWatchingSports": true,
                    "parkingOptions": {
                        "freeParkingLot": true
                    }
                }
            },
            "3": {
                "Breakfast": {
                    "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI",
                    "formattedAddress": "2512 Guardian Rd NW, Edmonton, AB T5T 1K8, Canada",
                    "location": {
                        "latitude": 53.5095095,
                        "longitude": -113.674498
                    },
                    "rating": 4.1,
                    "websiteUri": "https://www.originaljoes.ca/en/locations/ab/edmonton/2512-guardian-road-nw",
                    "priceLevel": "PRICE_LEVEL_MODERATE",
                    "userRatingCount": 746,
                    "displayName": {
                        "text": "Original Joe's",
                        "languageCode": "en"
                    },
                    "takeout": true,
                    "delivery": true,
                    "dineIn": true,
                    "curbsidePickup": false,
                    "reservable": true,
                    "servesBreakfast": true,
                    "servesLunch": true,
                    "servesDinner": true,
                    "servesBeer": true,
                    "servesWine": true,
                    "servesBrunch": true,
                    "servesVegetarianFood": true,
                    "photos": [
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFiN5xV069rThN_-8DLfl9LlBDApgX5LW_P8_xH8XcHP7wbRu3ulsxHak8RHaXbUnaRGOjOqSOb35x6Y5xkPl6EFz0amsrJzaQP-kOhTZQM7GHQwo8kdBJZ3487IwLHbbGayFdiP5ykv05VHnkYmBD9XyVwsGP5bBh8S"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjMbrYEmRJe3-rEqyP0vJnpZOkU2f2CO3_G7uUfKnT9BmLDC4_09ihXuooqOCKG4_p9mVU8Z3EBR0LfLxha9MKBuwCezPEsajOmWbjtqqHdXsKa3MnxO9zeoFGbWij6J4qbLIcbUja59baWh_fANxXmGA5BiK5H4irz"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFgV2T4whyEXjoWqwavWBTVGtp8khs05pvHl9VwjOfSBW4gfPVlYs9Q6BJIHtq9QzhgQu4Gb9IrrItK_gY6AjXK7YpQS-aKu95TOOPmOjeMmAVskGcf10ErIVzJIn0dFMwH2NkibrROPHyg2U39wYGzZKem9O6KmtkGH"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhso9qFV3FIJ-ajomN_Sr8jRiIUhRkfuBxHkTHLn8RlGlqVrvpIddsUtafL_lpuZeisRAL2Rcg7IDRAxJnS6H80pzKojjBsNrV2mieNgUV3opClsd04SqrJtXL6i2jWlkBvY3cnyepozKTxC16nfjFoFaptSgQ9yekp"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFj1KzL4-Flk0ExgNRkO6NgaqMCuTa6IfjW4G6PVly1RkMhsyraaANTay14IwItwB7E1x-GpuPkSGTrPcNQyC5-AXjQH_DowpLgsostXL5bdpxeoKDA9l0jBQp1kmkCotQjjxyuDtomSKdIOA7Moc4obCq6RH7ls30Mn"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhd_Oj4Rf1hk5q4uTo7oggUQaKMvuR4Nj4BAe40xwF41_WX6540yARbu325CdghlniMvRIQVMug9Fvp3ZRSXdSSv68SdnDL3cUd4zo0Cnpg2I3tY5GpD7reio1sVYW7-EN-SaNsQo4GQ12NyJ4raPqGF8G0SHPiNxpr"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhDzPm-nPm72rFGpeprlM8g5rB4WFW3Dtkf3Jffd73Vs0FJw7DWVyfbzedlIXP6HEE9I0WyYllEBAm4S_K_h-JZE-Q8aLKOpkDBgxuZ7oeCEagH2njJc1NvGR7eBbBFBbNHSi9u540tUelswxs8AR2mMqsJpTwTx8i-"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjcGeVjY27Y66HPJXs73sS2NoDmgsTkkXUsLR57t_Qqdy7iafvpOv1usVo7yTUoUvL_t2jwfj5mI11gndiOEyv0S_XTclm9elso_YniuR792yHOZyNa-K32Y0kS5m3uGd0caK8kU9lJUk03KhM31MkuRil8_TF4YReU"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhi8xJ7oeX0ZtKxcyXuMs5O7UxHWlTn7YTP9X4OTr-iW-rPxlg3qFAAX3YGfb02M6gqQQDXX60KpqI64t1qJs1hXn5MmqE8uwVAs0q9R7zUdLSxyZJyItsV1OQN1IsjGhASKJKBnq88gzeoCg_7zHASkdhYop5dCyOb"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFilr4Eh1s9ryi5frFDXL8iVpSflnVJAvvR9Cjk6EV3bic9qb5nuBkIYmaqJBnJ4AxlOoCM-ZH1vJrdQTunNwjnwWgJNIP9Th_2xMbiwsGIZZ2f-s2R7S_-2fYhZTYv7kplU9NsNgxSLWf2ya8Ybrou6lC3-VTTTNrfm"
                        }
                    ],
                    "outdoorSeating": true,
                    "liveMusic": false,
                    "menuForChildren": true,
                    "servesCocktails": true,
                    "servesDessert": true,
                    "servesCoffee": true,
                    "goodForChildren": false,
                    "restroom": true,
                    "goodForGroups": true,
                    "goodForWatchingSports": true,
                    "parkingOptions": {
                        "freeParkingLot": true
                    }
                },
                "Lunch": {
                    "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI",
                    "formattedAddress": "2512 Guardian Rd NW, Edmonton, AB T5T 1K8, Canada",
                    "location": {
                        "latitude": 53.5095095,
                        "longitude": -113.674498
                    },
                    "rating": 4.1,
                    "websiteUri": "https://www.originaljoes.ca/en/locations/ab/edmonton/2512-guardian-road-nw",
                    "priceLevel": "PRICE_LEVEL_MODERATE",
                    "userRatingCount": 746,
                    "displayName": {
                        "text": "Original Joe's",
                        "languageCode": "en"
                    },
                    "takeout": true,
                    "delivery": true,
                    "dineIn": true,
                    "curbsidePickup": false,
                    "reservable": true,
                    "servesBreakfast": true,
                    "servesLunch": true,
                    "servesDinner": true,
                    "servesBeer": true,
                    "servesWine": true,
                    "servesBrunch": true,
                    "servesVegetarianFood": true,
                    "photos": [
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFiN5xV069rThN_-8DLfl9LlBDApgX5LW_P8_xH8XcHP7wbRu3ulsxHak8RHaXbUnaRGOjOqSOb35x6Y5xkPl6EFz0amsrJzaQP-kOhTZQM7GHQwo8kdBJZ3487IwLHbbGayFdiP5ykv05VHnkYmBD9XyVwsGP5bBh8S"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjMbrYEmRJe3-rEqyP0vJnpZOkU2f2CO3_G7uUfKnT9BmLDC4_09ihXuooqOCKG4_p9mVU8Z3EBR0LfLxha9MKBuwCezPEsajOmWbjtqqHdXsKa3MnxO9zeoFGbWij6J4qbLIcbUja59baWh_fANxXmGA5BiK5H4irz"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFgV2T4whyEXjoWqwavWBTVGtp8khs05pvHl9VwjOfSBW4gfPVlYs9Q6BJIHtq9QzhgQu4Gb9IrrItK_gY6AjXK7YpQS-aKu95TOOPmOjeMmAVskGcf10ErIVzJIn0dFMwH2NkibrROPHyg2U39wYGzZKem9O6KmtkGH"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhso9qFV3FIJ-ajomN_Sr8jRiIUhRkfuBxHkTHLn8RlGlqVrvpIddsUtafL_lpuZeisRAL2Rcg7IDRAxJnS6H80pzKojjBsNrV2mieNgUV3opClsd04SqrJtXL6i2jWlkBvY3cnyepozKTxC16nfjFoFaptSgQ9yekp"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFj1KzL4-Flk0ExgNRkO6NgaqMCuTa6IfjW4G6PVly1RkMhsyraaANTay14IwItwB7E1x-GpuPkSGTrPcNQyC5-AXjQH_DowpLgsostXL5bdpxeoKDA9l0jBQp1kmkCotQjjxyuDtomSKdIOA7Moc4obCq6RH7ls30Mn"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhd_Oj4Rf1hk5q4uTo7oggUQaKMvuR4Nj4BAe40xwF41_WX6540yARbu325CdghlniMvRIQVMug9Fvp3ZRSXdSSv68SdnDL3cUd4zo0Cnpg2I3tY5GpD7reio1sVYW7-EN-SaNsQo4GQ12NyJ4raPqGF8G0SHPiNxpr"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhDzPm-nPm72rFGpeprlM8g5rB4WFW3Dtkf3Jffd73Vs0FJw7DWVyfbzedlIXP6HEE9I0WyYllEBAm4S_K_h-JZE-Q8aLKOpkDBgxuZ7oeCEagH2njJc1NvGR7eBbBFBbNHSi9u540tUelswxs8AR2mMqsJpTwTx8i-"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFjcGeVjY27Y66HPJXs73sS2NoDmgsTkkXUsLR57t_Qqdy7iafvpOv1usVo7yTUoUvL_t2jwfj5mI11gndiOEyv0S_XTclm9elso_YniuR792yHOZyNa-K32Y0kS5m3uGd0caK8kU9lJUk03KhM31MkuRil8_TF4YReU"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFhi8xJ7oeX0ZtKxcyXuMs5O7UxHWlTn7YTP9X4OTr-iW-rPxlg3qFAAX3YGfb02M6gqQQDXX60KpqI64t1qJs1hXn5MmqE8uwVAs0q9R7zUdLSxyZJyItsV1OQN1IsjGhASKJKBnq88gzeoCg_7zHASkdhYop5dCyOb"
                        },
                        {
                            "name": "places/ChIJf9dmmoSKn1MR8bn52VkR-ZI/photos/AWU5eFilr4Eh1s9ryi5frFDXL8iVpSflnVJAvvR9Cjk6EV3bic9qb5nuBkIYmaqJBnJ4AxlOoCM-ZH1vJrdQTunNwjnwWgJNIP9Th_2xMbiwsGIZZ2f-s2R7S_-2fYhZTYv7kplU9NsNgxSLWf2ya8Ybrou6lC3-VTTTNrfm"
                        }
                    ],
                    "outdoorSeating": true,
                    "liveMusic": false,
                    "menuForChildren": true,
                    "servesCocktails": true,
                    "servesDessert": true,
                    "servesCoffee": true,
                    "goodForChildren": false,
                    "restroom": true,
                    "goodForGroups": true,
                    "goodForWatchingSports": true,
                    "parkingOptions": {
                        "freeParkingLot": true
                    }
                }
            }
        }
    }
    """
    outputs = json.loads(s.strip())
    results = outputs["results"]
    days = []
    for i in range(3):
        day = {"meals": []}
        day["name"] = f'Day {i+1}'
        for k, v in results[str(i+1)].items():
            v["meal_name"] = k
            day["meals"].append(v)
        days.append(day)

    return {
        "days": days,
    }


print(main({}))

{ % for i in outputs.days % }
{ % for m in i.meals % }
{{m.meal_name}}
{ % endfor % }
{ % endfor % }
