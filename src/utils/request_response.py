# requests_res.py
import requests
from requests.exceptions import RequestException
from urllib.parse import urljoin

def safe_get(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the response status code is 4XX/5XX
        return response
    except RequestException as e:
        print(f"Request failed: {e}")
        return None
