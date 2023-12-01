#!/usr/bin/python3
"""define url module"""

import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    id_req = dict(r.headers).get("X-Request-Id")
    print(id_req)
