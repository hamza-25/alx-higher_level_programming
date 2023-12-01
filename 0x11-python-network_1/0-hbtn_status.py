#!/usr/bin/python3
"""define url module"""


if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        print("Body response:\n\t- type: {}\n\t- content: b'{}'".format(
            type(resp.read()), resp.msg))
        print("\t- utf8 content: {}".format(resp.read().decode('utf-8')))
