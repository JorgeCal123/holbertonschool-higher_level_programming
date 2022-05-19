#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""
import urllib.request as request
from sys import argv

if __name__ == "__main__":
    url = request.Request(argv[1])
    with request.urlopen(url) as r:
        print(r.getheader('X-Request-Id'))
