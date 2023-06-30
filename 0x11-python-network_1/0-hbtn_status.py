#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        data = r.read()
        print('Body response:')
        print("\t- type: {}".format(type(r)))
        print("\t- content: {}".format(r))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
