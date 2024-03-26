import os
from serpapi import GoogleSearch

def find_company_website(company_name):
    api_key = os.environ.get('SERP_API_KEY')
    if not api_key:
        print("SERP_API_KEY environment variable is not set.")
        return "Website not found due to missing API key."
    
    params = {
        "q": company_name,
        "google_domain": "google.com",
        "hl": "en",
        "api_key": api_key,
        "num": "10"  # Increase the number of results to ensure we have enough to choose from
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results.get("organic_results", [])
        
        for result in organic_results:
            link = result.get("link", "")
            if "wikipedia" not in link:
                return link  # Return the first non-Wikipedia link
        return "Website not found."  # Return this if no non-Wikipedia links are found
    
    except Exception as e:
        print(f"Error finding website for {company_name}: {e}")
        return "Website not found due to error."