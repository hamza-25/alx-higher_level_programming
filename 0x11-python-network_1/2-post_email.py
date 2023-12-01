#!/usr/bin/python3
"""define url module"""

import urllib.request as request
import urllib.parse as parse
import sys
if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    url = sys.argv[1]
    convert = parse.urlencode(email).encode("ascii")
    req = request.Request(url, convert)
    with request.urlopen(req) as f:
        print(f.read().decode('utf-8'))
