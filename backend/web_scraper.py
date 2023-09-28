from gensim.summarization import summarize
import requests
from bs4 import BeautifulSoup
import random

# WEB SCRAPER & SUMMARIZER

def scrape_website(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the desired information from the parsed HTML
        # Customize this part based on the structure of the webpage
        # and the specific information you want to retrieve
        # Here's an example of extracting all the text from <p> tags:
        paragraphs = soup.find_all('p')
        extracted_data = [p.get_text() for p in paragraphs]
        combined_data = " ".join(extracted_data)
        # print(extracted_data)
        if len(extracted_data) >= 20:
            return summarize(combined_data, word_count=20)
        else:
            return summarize(combined_data, ratio=0.2)
    else:
        # Request was unsuccessful, handle the error accordingly
        print('Error:', response.status_code)

# Example usage
# url = 'https://www.ucc.edu/admissions/paying-for-college/'
# data = scrape_website(url)
# print( scrape_website(url) )

# # print( summarize(data) )

# # # Check if the data is not None before summarizing
# if data:
#     # Adjust ratio and split to introduce randomness
#     ratio = random.uniform(0.1,0.2) # Random ratio between 10% and 30%
#     summarized_data = summarize(data, ratio=ratio)
#     print(summarized_data)
# else:
#     print('No data found')

