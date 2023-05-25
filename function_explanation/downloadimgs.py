import davipy as dv #import the library

#define the url
url = "https://www.ebay.it/"

#put your ulr in the function
dv.downloadallimg(url)

#run your python file


#for example you can use it in a list of links

links = ["https://www.mangaworld.bz/","https://www.freeimages.com/","https://www.womeng2g.org/"]

for site in links:
    dv.downloadallimg(site)