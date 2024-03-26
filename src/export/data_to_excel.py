import pandas as pd


def write_filtered_pdfs_to_file(company_websites):
    data_for_df = []
    for (name, website), pdfs in company_websites.items():
        for pdf in pdfs:
            data_for_df.append({'Name': name, 'Website': website, 'PDF': pdf})

    # Create a DataFrame
    df = pd.DataFrame(data_for_df)

    # Write the DataFrame to an Excel file
    excel_filename = './data/output/company_websites_expanded.xlsx'
    df.to_excel(excel_filename, index=False)
