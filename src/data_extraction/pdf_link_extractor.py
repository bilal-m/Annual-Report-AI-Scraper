import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(url):
    # write causes that causes scraping to freeze
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


def filter_pdf_links(links):
    keywords = ["finance", "financial", "financialreport"]
    filtered_pdf_links = []
    for link in links:
        if link.strip().lower().endswith('.pdf'):
            if any(keyword in link.strip().lower() for keyword in keywords):
                filtered_pdf_links.append(link)
    return filtered_pdf_links

def crawl_for_pdfs(url, depth, visited=None):
    if visited is None:
        visited = set()
    if url in visited or depth == 0:
        return []
    print(f"Crawling: {url}")
    visited.add(url)
    pdf_links = []
    
    links = get_all_links(url)
    pdf_links.extend(filter_pdf_links(links))
    
    for link in links:
        if link not in visited:
            pdf_links.extend(crawl_for_pdfs(link, depth - 1, visited))
    
    return list(set(pdf_links))

def write_pdfs_to_file(website, pdfs):
    filename = f"pdf_links_{website.replace('http://', '').replace('https://', '').split('/')[0]}.txt"
    with open(filename, 'w') as file:
        for pdf in pdfs:
            print(pdf)  # Print each PDF link
            file.write(pdf + '\n')
    print(f"PDF links for {website} have been written to {filename}")
    

if __name__ == "__main__":
    start_url = "https://www.atlascopcogroup.com/"

    pdfs = crawl_for_pdfs(start_url, depth=2)
    
    write_pdfs_to_file(start_url, pdfs)
