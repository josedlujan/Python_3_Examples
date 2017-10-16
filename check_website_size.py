import urllib.request as request
link = "https://python.org"
print ("url:", link)
site = request.urlopen(link)
meta = site.info()
print ("Content-Length:", site.headers['content-length'])

#Create the file out.txt before script execute
f = open("out.txt", "r")
print ("File on disk:",len(f.read()))
f.close()

f = open("out.txt", "wb")
f.write(site.read())
site.close()
f.close()

f = open("out.txt", "r")
print ("File on disk after download:",len(f.read()))
f.close()

print ("os.stat().st_size returns:", os.stat("out.txt").st_size)
