#!/usr/bin/python3
"""define url module"""

import urllib.request as request
import urllib.parse as parse
import urllib.error as error
import sys
if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
