#!/usr/bin/python3
"""define url module"""

import urllib.request as request
if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as f:
        resp = f.read()
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(resp), resp))
    print("\t- utf8 content: {}".format(resp.decode('utf-8')))
