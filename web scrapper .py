import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # This example looks for <h2> tags (common for headlines)
    # You can change 'h2' to 'h1' or 'h3' depending on the site
    headlines = soup.find_all('h2')
    
    print(f"\n--- Latest Headlines from {url} ---")
    for i, title in enumerate(headlines[:10], 1):
        print(f"{i}. {title.get_text().strip()}")

if __name__ == "__main__":
    target_site = "https://bbc.com" # Example URL
    scrape_headlines(target_site)
