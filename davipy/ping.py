import requests
from requests.exceptions import ConnectionError


def ping(link: str) -> bool:
    """docstring"""  # TODO scrivila
    try:
        requests.get(link)
    except ConnectionError:
        return False
    return True
