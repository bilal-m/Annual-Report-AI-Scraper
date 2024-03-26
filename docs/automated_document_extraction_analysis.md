
## Choosing SerpAPI over LLM for Website Searches

Using SerpAPI for searching websites by company name offers a distinct advantage over using Large Language Models (LLMs) for this purpose. SerpAPI is specifically designed to interact with search engines and retrieve real-time, accurate search results. This is particularly important for tasks where up-to-date information is crucial, such as finding the current official website of a company. SerpAPI provides structured search results, making it easier to extract specific information like website URLs. In contrast, LLMs might provide outdated information or lack the precision in directly fetching current website URLs from a vast knowledge base. Hence, for tasks requiring current and specific web search results, SerpAPI is the preferred tool.


# Automated Document Extraction and Analysis

## Overview

The project aims to automate the process of extracting and analyzing documents from company websites. Specifically, it focuses on:

1. **Getting websites** of companies.
2. **Extracting PDF/Doc/File links** from those sites.
3. **Downloading** these documents.
4. **Scanning PDFs** for relevant data, such as financial statements.

## Implementation Steps

### Step 1: Get the Websites

Use SerpAPI and Google Search to find company websites based on company names.

### Step 2: Get the PDF/Doc/File Links from the Site

Extract PDF links from the websites. Ensure to log the found PDF links for debugging purposes.

### Step 3: Download the PDFs

Download the PDF files from the extracted links to a specified directory for further processing.

### Step 4: Scan PDFs for Relevant Data

Analyze the downloaded PDFs to extract text and search for specific sections or keywords relevant to the project's goals, such as "financial statement".

## Handling Edge Cases

- **Obscure Web Stacks and Uncommon File Formats**: The solution primarily targets common file paths and formats. Handling forms or uncommon formats may require custom solutions.

- **Non-English PDFs**: For PDFs in languages other than English, consider using a translation API to detect and translate content as needed.

## Automation Limitations

- **Automated for**: The script is designed to handle common website structures and PDF formats, especially those containing keywords like "financial statement".

- **Not automated for**: The script may not automatically handle websites that require form submissions to access files, or non-English documents without integrating additional translation steps.
