#!/usr/bin/python3
"""define url module"""

import urllib.request as request
import sys
if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as f:
        print(dict(f.headers).get('X-Request-Id'))
