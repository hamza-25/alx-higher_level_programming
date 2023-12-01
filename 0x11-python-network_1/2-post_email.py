#!/usr/bin/python3
"""define url module"""

import urllib.request as request
import sys
if __name__ == "__main__":
    url = sys.argv[1] + '?email=' + sys.argv[2]
    with request.urlopen(url) as f:
        print(f.read())
