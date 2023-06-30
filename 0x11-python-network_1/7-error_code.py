#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL & displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    resp = requests.get(argv[1])
    statuscode = resp.status_code
    if statuscode >= 400:
        print("Error code: {}".format(statuscode))
    else:
        print(resp.text)
