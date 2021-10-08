import requests, json, pytest
from asteroids.asteroid_closest_approach import asteroid_closest_approach

def test_asteroids_closest_approach():
    asteroids_json = asteroid_closest_approach(10)
    asteroids = json.loads(asteroids_json)

    for i in range(len(asteroids)):
        assert asteroids[i]['links']
        assert asteroids[i]['id']
        assert asteroids[i]['neo_reference_id']
        assert asteroids[i]['name']
        assert asteroids[i]['designation']
        assert asteroids[i]['nasa_jpl_url']
        assert asteroids[i]['close_approach_data']
        assert type(asteroids[i]['close_approach_data']) is dict
        # print(asteroids[i]['close_approach_data'])
        assert asteroids[i]['close_approach_data']['miss_distance']['astronomical']

