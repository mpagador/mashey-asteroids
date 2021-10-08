import requests

api_key = "k0XKqPcQ5dw74JLbhPpVuj4hjXItEllbPWpfn4eo"

def neo_feed(start_date, end_date):
    endpoint = "https://api.nasa.gov/neo/rest/v1/feed?start_date={}&end_date={}&api_key={}".format(
        start_date, end_date, api_key)
    return requests.get(endpoint).json()

def neo_lookup(asteroid_id):
    endpoint = "https://api.nasa.gov/neo/rest/v1/neo/{}?api_key={}".format(asteroid_id, api_key)
    return requests.get(endpoint).json()

def neo_browse(page=0):
    endpoint = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={}&page={}".format(api_key, page)
    return requests.get(endpoint).json()
