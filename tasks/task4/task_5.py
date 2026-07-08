import requests
from typing import Tuple

def make_request(url: str) -> Tuple[int, str]:
    try:
        response = requests.get(url)
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)