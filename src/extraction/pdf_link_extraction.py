from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import concurrent.futures
from src.utils.request_response import safe_get

def extract_links(url):
    response = safe_get(url)
    if response is None:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    return [urljoin(url, link['href']) for link in soup.find_all('a', href=True)]

def get_all_links_with_timeout(url, timeout=10):
    """Attempt to get all links within a specified timeout."""
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(get_all_links, url)
        try:
            return future.result(timeout=timeout)
        except concurrent.futures.TimeoutError:
            print(f"Timeout occurred while trying to get links from {url}")
            return []
        except Exception as e:
            print(f"Error occurred: {e}")
            return []
        
def get_all_links(url):
    if url == "https://www.pekaobiznes24.pl/do/LangSelect":
        print("Skipping problematic URL")
        return []
    else:
        links = []
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                full_link = urljoin(url, link['href'])
                links.append(full_link)
        except Exception as e:
            print(f"Failed to get links from {url}: {e}")
        return links

