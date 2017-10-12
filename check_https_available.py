import urllib.request as request
req = request.Request('http://python.org')
res = request.urlopen(req)
print("HTTP or HTTPS: ", res.geturl())