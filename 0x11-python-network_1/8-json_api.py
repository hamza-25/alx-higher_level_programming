#!/usr/bin/python3
"""define url module"""

import requests
import sys
if __name__ == "__main__":
    q = ''
    if sys.argv[1]:
        q = sys.argv[1]
    payload = {"q": q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    if isinstance(r, dict) and len(r) == 0:
        print("No result")
    elif isinstance(r, dict):
        print("[{}] {}".format(r['id'], r['name']))
    else:
        print("Not a valid JSON")
