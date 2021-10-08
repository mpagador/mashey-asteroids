import json, pytest
from asteroids.nearest_misses import nearest_misses

def test_nearest_misses():
    asteroids_json = nearest_misses(10)
    asteroids = json.loads(asteroids_json)
    assert len(asteroids) == 10

    lowest = 0.0
    for i in range(len(asteroids)):
        assert asteroids[i]['close_approach_data']
        assert asteroids[i]['close_approach_data']['miss_distance']['astronomical']
        current_miss = float(asteroids[i]['close_approach_data']['miss_distance']['astronomical'])
        assert lowest < current_miss
        lowest = current_miss

        assert asteroids[i]['links']
        assert asteroids[i]['id']
        assert asteroids[i]['neo_reference_id']
        assert asteroids[i]['name']
        assert asteroids[i]['designation']
        assert asteroids[i]['nasa_jpl_url']
        assert asteroids[i]['close_approach_data']
        assert type(asteroids[i]['close_approach_data']) is dict
