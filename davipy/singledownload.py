import requests


def imgsingledownload(url):
    """blabla"""  # TODO docstring
    sito = requests.get(url)
    nome_img = url.split("/")[-1]
    with open(nome_img, "wb") as f:
        f.write(sito.content)
