import json
from .asteroid_closest_approach import asteroid_closest_approach

def nearest_misses(page_limit):
    asteroids = json.loads(asteroid_closest_approach(page_limit))
    asteroids.sort(key=lambda k: k['close_approach_data']['miss_distance']['astronomical'])
    nearest = asteroids[:10]
    return json.dumps(nearest)

