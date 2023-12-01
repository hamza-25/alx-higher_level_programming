#!/usr/bin/python3
""" """


if __name__ == "__main__":
    import urllib.request as request
    resp = request.urlopen("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: b'{}'".format(type(resp.read()), resp.msg))
    print("\t- utf8 content: {}".format(resp.msg))

