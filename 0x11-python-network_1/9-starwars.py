#!/usr/bin/python3

"""
star wars api
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get("https://swapi.co/api/people/?search=" + argv[1])
    if "json" not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        res = r.json()
        search_res = res.get('results')
        print("Number of results: " + str(res.get('count')))
        for r in search_res:
            print(r.get('name'))
