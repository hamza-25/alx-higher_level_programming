#!/usr/bin/python3
"""define url module"""

import requests
import sys
if __name__ == "__main__":
    url = "https://api.github.com/users"
    header = {"Authorization": f'token {sys.argv[2]}'}
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        r_json = r.json()
        user_id = r_json.get('id')
        print(user_id)
    else:
        print(None)
