import requests
import fitz
from langdetect import detect, LangDetectException
from src.crawler.translator import TranslationDict
from src.export.data_to_excel import append_pdf_to_excel

def detect_language(text):
    try:
        return detect(text)
    except LangDetectException as e:
        print(f"Language detection failed: {e}")
        return None   

def filter_pdf_links(company_name, website, links, visited_pdf_links):
    translation_dict = TranslationDict()
    translated_keywords = translation_dict.translated_keywords
    url_contains_keyword = False   
    content_contains_keyword = False  
    filtered_pdf_links_struct = []
    print("Filtering pdf links by keywords...")
    for link in links:
        if not link in visited_pdf_links:
            # Scan URLs for keywords
            visited_pdf_links.append(link)
            for keyword in  ["finance", "financial", "financial report"]:
                if keyword in link:
                    print("Text contains translated keyword:", keyword)
                    url_contains_keyword = True
                    break

            # If the URL does not contain keywords, scan the PDF content
            if not url_contains_keyword:
                text = pdf_word_scanner(link, keyword)
                if text:
                    try:
                        detected_language = detect(text)
                    
                        # Now scan the translated text for keywords
                        for keyword in translated_keywords.get(detected_language, []):
                            if keyword in text.lower():
                                print("PDF content contains keyword after translation")
                                content_contains_keyword = True
                                break
                    except Exception as e:
                        continue

            if content_contains_keyword or url_contains_keyword:
                append_pdf_to_excel(company_name, website, link, "Scraped-Website-PDFs")
            
                filtered_pdf_links_struct.append({
                    "company_name": company_name,
                    "website": website,
                    "pdf_link": link
                })
        else:
            continue 
    return filtered_pdf_links_struct
        


async def filter_given_pdf_links(company_name, link):

    translation_dict = TranslationDict()
    translated_keywords = translation_dict.translated_keywords
    url_contains_keyword = False   
    content_contains_keyword = False  
    filtered_pdf_links_struct = []
    
    for keyword in  ["finance", "financial", "financial report"]:
        if keyword in link:
            print("Text contains translated keyword:", keyword)
            url_contains_keyword = True
            break

    if content_contains_keyword or url_contains_keyword:
        append_pdf_to_excel(company_name, None, link, "Filtered-PDFs-Given-in-Sheet")
        filtered_pdf_links_struct.append({
            "company_name": company_name,
            "pdf_link": link
        })
    append_pdf_to_excel(company_name, "-", link, "Filtered-PDFs-Given-in-Sheet")
    
    return filtered_pdf_links_struct

def pdf_word_scanner(pdf_url, keyword):
    print("Scanning inside the pdf...")
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
        
        with fitz.open(stream=response.content, filetype="pdf") as doc:
            for page in doc:
                text = page.get_text()
                if keyword.lower() in text.lower():
                    print("Keyword found in the document.")
                    return text  # Return text of the first page where the keyword is found
        print("Keyword not found in the document.")
    except Exception as e:
        print(f"Failed to scan {pdf_url}: {e}")
        return ""
    return "" 