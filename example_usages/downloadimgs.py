import davipy as dv


# single link example
url = "https://www.ebay.it/"
dv.downloadallimg(url)

# list of links example
links = ["https://www.mangaworld.bz/", "https://www.freeimages.com/", "https://www.womeng2g.org/"]

for site in links:
    dv.downloadallimg(site)
