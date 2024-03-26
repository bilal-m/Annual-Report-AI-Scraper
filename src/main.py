from data_extraction.company_name_extractor import extract_company_names_from_excel
from data_extraction.pdf_link_extractor import crawl_for_pdfs
from data_extraction.company_website_extractor import find_company_website
from data_processing.process_pdfs import analyze_url_for_financial_content
from export.data_to_excel import write_filtered_pdfs_to_file

def main():
    company_names = extract_company_names_from_excel("./data/input/ai_automation_project.xlsx")
    process_company_pdfs(company_names)

def process_company_pdfs(company_names):
    company_websites = {}

    # company_websites = {}
    # for name in company_names:
    #     website = find_company_website(name)
    #     company_websites[(name, website)] = []
    #     print(f"{name}: {website}")
    #     if website != "Website not found.":
    #         pdfs = crawl_for_pdfs(website, depth=2)
    #         if pdfs:
    #             company_websites[(name, website)] = pdfs


    # TEST: this is mock company website list
    mock_websites = ['https://www.bancsabadell.com/bsnacional/es/particulares/', 'https://www.ems-group.com/en/about-ems/about-ems/ems-at-a-glance/', 'https://www.swisslife.com/en/home.html', 'https://worldline.com/', 'https://www.givaudan.com/']         
    mock_websites_2 = ['https://www.bancsabadell.com/bsnacional/es/particulares/', 'https://www.ems-group.com/en/about-ems/about-ems/ems-at-a-glance/']         
    mock_websites_3 = [('swisslife', 'https://www.swisslife.com/en/home.html'), ('worldline', 'https://worldline.com/'), ('givaudan','https://www.givaudan.com/')]         
    mock_websites_4 = [('givaudan','https://www.givaudan.com/')]         

    for (name, website) in mock_websites_3:
        if website != "Website not found.":
            pdfs = crawl_for_pdfs(website, depth=2)
            if pdfs:
                company_websites[(name, website)] = pdfs
                print(f"{website}: {pdfs}")

    write_filtered_pdfs_to_file(company_websites)

    
    # #uncomment when using serp api getting pdfs for websites
    # result = {} 
    # for website, pdfs in company_pdfs.items():
    #     result[website] = []
    #     for pdf_url in pdfs:
    #         result[website].append(analyze_url_for_financial_content(pdf_url))
    #     print(f"Website {website},\npdfs containing finance related keywords: {result[website]}\n\n")

if __name__ == "__main__":
    main()
