import json
from .neows import neo_browse

def asteroid_closest_approach(page_limit=0):
    original_data = neo_browse()
    cleaned_data = []
    pages = original_data['page']['total_pages']
    if page_limit == 0:
        page_limit = pages

    # originally used pages, but using page_limit to avoid going over API limit & test code
    for page in range(page_limit):
        original_data = neo_browse(page)
        for neo in original_data['near_earth_objects']:
            if neo['close_approach_data']:
                neo['close_approach_data'] = min(neo['close_approach_data'],
                                             key=lambda k: k['miss_distance']['astronomical'])
                cleaned_data.append(neo)

    return json.dumps(cleaned_data)
