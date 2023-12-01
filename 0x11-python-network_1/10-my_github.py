#!/usr/bin/python3
"""define url module"""

import requests
import sys
if __name__ == "__main__":
    url = f'https://api.github.com/user/{sys.argv[1]}'
    headers = {"Authorization": f'token {sys.argv[2]}'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        r_json = r.json()
        user_id = r_json.get('id')
        print(user_id)
    else:
        print(None)
