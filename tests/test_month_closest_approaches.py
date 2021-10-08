import requests, json, pytest
from asteroids.month_closest_approaches import month_closest_approaches

# YEAR-MONTH-DAY, 0000-00-00
def test_month_closest_approaches():
    asteroids_json = month_closest_approaches('2021-01-01')
    asteroids = json.loads(asteroids_json)
    assert asteroids['start_date'] == '2021-01-01'
    assert list(asteroids.keys()) == ['start_date', 'element_count', 'near_earth_objects']
    assert int(asteroids['element_count'])
    assert len(list(asteroids['near_earth_objects'])) == 31


