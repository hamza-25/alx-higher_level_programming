#!/usr/bin/python3
"""define url module"""

import requests
import sys
if __name__ == "__main__":
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    r = requests.get(url)
    if r.status_code == 200:
        r_json = r.json()
        count = 0
        for commit in r_json:
            print("{}: {}".format(
                commit['sha'], commit['commit']['author']['name']))
            if count == 9:
                break
            count += 1
