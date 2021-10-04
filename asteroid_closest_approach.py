import json, NeoWs

def asteroid_closest_approach():
    original_data = NeoWs.neo_browse()
    cleaned_data = []

    for neo in original_data["near_earth_objects"]:
        neo["close_approach_data"] = min(neo["close_approach_data"],
                                         key = lambda k: k["miss_distance"]["astronomical"])
        cleaned_data.append(neo)

    return json.dump(cleaned_data)
