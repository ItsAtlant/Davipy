import requests
from bs4 import BeautifulSoup
import os


def listlink(url: str) -> None:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    foldername = url.split(".")[1] + "_siti"
    os.makedirs(foldername, exist_ok=True)

    with open(f"{foldername}/siti.txt", "w") as f:
        f.write("I link sono:\n")
        for link in soup.find_all("a"):
            sololink = str(link.get("href"))
            if sololink.startswith("http"):  # It accepts "https" too
                f.write(sololink + "\n")
