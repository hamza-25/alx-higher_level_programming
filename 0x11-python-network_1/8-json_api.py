#!/usr/bin/python3
"""define url module"""

import requests
import sys
if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    payload = {"q": q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    r_json = r.json()
    if isinstance(r_json, dict) and len(r_json) == 0:
        print("No result")
    elif isinstance(r_json, dict):
        print("[{}] {}".format(r_json['id'], r_json['name']))
    else:
        print("Not a valid JSON")
