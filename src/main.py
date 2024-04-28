import time

import aiohttp
from src.extraction.company_pdf_extractor import extract_ei_pairs_from_excel

from src.crawler.pdf_crawler import crawl_for_pdfs
from src.extraction.company_website_extractor import find_company_website
import asyncio
from aiohttp import TCPConnector
from src.crawler.pdf_processing import filter_given_pdf_links

async def main():
    # extract company names from excel by Serp API
    # company_names = extract_company_names_from_excel("./data/input/ai_automation_project.xlsx")

    """
    Task 1:
    Links can be filtered by determining if they contain specific English keywords.
    In cases where no English word is detected in the title, the algorithm examines the content of the PDF for optimization purposes. 
    It then checks for the presence of finance-related words across all European languages.
    The output is saved to the "llm-project/data/output/"Filtered-PDFs-Given-in-Sheet".xlsx" directory.
    """
    # await process_company_pdfs()

    """
    From the provided Excel input, the algorithm scans the given PDF links to filter out those containing finance-related words in their URLs. 
    The output is saved to the "llm-project/data/output/Scraped-Website-PDFs.xlsx" directory.
    """ 
    await process_given_company_pdfs()

async def process_company_pdfs():
    company_websites = [('Segro', 'https://www.segro.com/')]
    connector = TCPConnector(limit=10)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        visited_pdf_links = []
        for (name, website) in company_websites:
            print(f"Start scraping pdfs for {name} by the website {website}")
            if website != "Website not found.":
                # Create task for each website
                task = crawl_for_pdfs(name, website, website, visited_pdf_links, depth=2, session=session)
                tasks.append(task)

        # Await tasks and gather results
        results = await asyncio.gather(*tasks)

        # Process and print results``
        for result in results:
            # Assuming result is a list of PDF URLs
            for pdf_url in result:
                print(pdf_url)
     
async def process_given_company_pdfs():    
    company_pdfs = extract_ei_pairs_from_excel()

    connector = TCPConnector(limit=10)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for (name, pdf) in company_pdfs:
            if pdf != "Website not found.":
                task = filter_given_pdf_links(name, pdf)
                tasks.append(task)

        # Await tasks and gather results
        results = await asyncio.gather(*tasks)

        # Process and print results
        for result in results:
            # Assuming result is a list of PDF URLs
            for pdf_url in result:
                print(pdf_url)
     
if __name__ == "__main__":
    start_time = time.time()
    print("Application is started: ")
    print(asyncio.run(main()))
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")


