from src.crawler.pdf_processing import filter_pdf_links
from ..extraction.pdf_link_extraction import get_all_links_with_timeout, get_all_links
import aiohttp
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


async def get_all_links_with_timeout(session, url):
    print("get_all_links_with_timeout")
    timeout = aiohttp.ClientTimeout(total=10)
    pdf_links = []
    non_pdf_links = []

    try:
        if url == "https://www.pekaobiznes24.pl/do/LangSelect":
            print("Skipping problematic URL")
            return pdf_links, non_pdf_links
        else:
            async with session.get(url, timeout=timeout) as response:
                print("parsing the page...")
                if 'text/html' in response.headers.get('Content-Type', '').lower():
                    text = await response.text()
                    soup = BeautifulSoup(text, 'lxml')
                    for link in soup.find_all('a', href=True):
                        full_link = urljoin(url, link['href'])
                        if full_link.lower().endswith('.pdf'):
                            pdf_links.append(full_link)
                        else:
                            non_pdf_links.append(full_link)
                elif 'application/pdf' in response.headers.get('Content-Type', '').lower():
                    pdf_links.append(full_link)

                return pdf_links, non_pdf_links
    except Exception as e:
        print(f"Request to {url} failed: {e}")
        return pdf_links, non_pdf_links
    
    
async def parse_links(html_content):
    # Given the HTML content, return all the href links found
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    return links

async def crawl_for_pdfs(company_name, website, url, visited_pdf_links, depth, session, visited=None, attempts=3):
    print("Crawling for pdfs...")
    if visited is None:
        visited = set()
    if url in visited or depth == 0:
        return []
    
    visited.add(url)
    pdf_links_websites_struct = []

    if len(visited) > 50: 
        return list(set(pdf_links_websites_struct))
    
    for _ in range(attempts):
        pdf_links, non_pdf_links = await get_all_links_with_timeout(session, url)
        if pdf_links:
            break
    else:
        print("Timeout - skipping this url: ", url)
        return list(set(pdf_links_websites_struct))

    pdf_links_websites_struct.extend(filter_pdf_links(company_name, website, pdf_links, visited_pdf_links))

    for link in non_pdf_links:
        if link not in visited:
            pdf_links_from_recursive_call = await crawl_for_pdfs(company_name, website, link, visited_pdf_links, depth - 1, session, visited)
            pdf_links_websites_struct.extend(pdf_links_from_recursive_call)

    return pdf_links_websites_struct
