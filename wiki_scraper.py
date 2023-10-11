import requests
from bs4 import BeautifulSoup

# Define the URL of the Wikipedia page you want to scrape
url = 'https://en.wikipedia.org/wiki/Web_scraping'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract all paragraphs containing text
    paragraphs = soup.find_all('p')

    # Combine and save the text of all paragraphs
    page_text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])

    # Save the entire text content to a file
    with open('scraped_wikipedia_text.txt', 'w', encoding='utf-8') as file:
        file.write(page_text)

    print('Entire Wikipedia page text has been saved to scraped_wikipedia_text.txt')
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
