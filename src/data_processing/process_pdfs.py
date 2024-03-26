from openai import OpenAI


def analyze_url_for_financial_content(url: str) -> str:
    client = OpenAI()
    prompt = f"Identify if the following text contains financial information: {url}"
    
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0,
        max_tokens=1024,
    )

    return response.choices[0].text.strip()