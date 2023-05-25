import davipy as dv #import the library

#define the url
url = "https://www.chess.com/"


#now you can see if its reacheable
print(dv.ping(url))


#you can even use it if you want to check a site before doing webscaping

if dv.ping(url) == "pong":
    dv.listlink(url)