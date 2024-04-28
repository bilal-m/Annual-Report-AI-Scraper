from bs4 import BeautifulSoup
from urllib.parse import urljoin
import aiohttp

async def is_pdf_link(session, url):
    try:
        async with session.head(url, allow_redirects=True) as response:
            return response.headers.get('Content-Type', '').lower() == 'application/pdf'
    except aiohttp.ClientError:
        return False

async def fetch_links(session, url, timeout=20):
    links = []  # This will store the final PDF links
    async with session.get(url, timeout=timeout) as response:
        if 'application/pdf' in response.headers.get('Content-Type', ''):
            text = await response.text()
            soup = BeautifulSoup(text, 'lxml')
            for link in soup.find_all('a', href=True):
                # Complete relative links
                full_link = urljoin(url, link['href'])
                if full_link not in links:  # Avoid re-checking duplicates
                    if full_link.lower().endswith('.pdf') or await is_pdf_link(session, full_link):
                        links.append(full_link)
    return links

async def main():
    url = "https://admiralgroup.co.uk/static-files/e914da16-f0fd-41e0-9571-6ec9df780e3c"  # Replace with your target URL
    async with aiohttp.ClientSession() as session:
        pdf_links = await fetch_links(session, url)
        print(pdf_links)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
