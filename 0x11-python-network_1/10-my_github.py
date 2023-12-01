#!/usr/bin/python3
"""define url module"""

import requests
from requests.auth import HTTPBasicAuth
import sys
if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=auth)
    if r.status_code == 200:
        r_json = r.json()
        user_id = r_json.get('id')
        print(user_id)
    else:
        print(None)
