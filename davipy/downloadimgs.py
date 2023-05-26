# from __future__ import annotations
import requests
from bs4 import BeautifulSoup
import os


def downloadallimg(url: str) -> dict:
    """
    Downloads all the images from the provided website
    :param url:
    :return:
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    images_links = []

    for link in soup.find_all("img"):
        images_links.append(link.get("data-src"))
        images_links.append(link.get("src"))

    foldername = url.split(".")[1] + "_img"
    os.makedirs(foldername, exist_ok=True)

    warnings_count, successful_requests_count = 0, 0

    for linkimg in images_links:
        if linkimg is None:
            continue

        imgname = linkimg.split("/")[-1]
        imgname = imgname.split("?")[0]

        try:
            response = requests.get(linkimg)
        except:  # TODO which SPECIFIC exception do you want to catch?
            warnings_count += 1

        with open(f"{foldername}/{successful_requests_count}__{imgname}", "wb") as f:
            f.write(response.content)
            successful_requests_count += 1

    return {
        "warnings": warnings_count,
        "saved": successful_requests_count,
        "total": warnings_count + successful_requests_count,
    }
