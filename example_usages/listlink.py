import davipy as dv


# single link example
url = "https://www.ebay.it/"
dv.listlink(url)

# link list example
links = ["https://www.mangaworld.bz/", "https://www.freeimages.com/", "https://www.womeng2g.org/"]
for site in links:
    dv.listlink(site)
