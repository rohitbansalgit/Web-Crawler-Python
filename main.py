import requests
from bs4 import BeautifulSoup
from lxml import html

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        self.page_content = self.fetch_page_content()

    def fetch_page_content(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to retrieve the content. Status code: {response.status_code}")

    def extract_multiple_classes(self, class_names):
        soup = BeautifulSoup(self.page_content, 'html.parser')
        for class_name in class_names:
            elements = soup.find_all(class_=class_name.strip())
            for element in elements:
                print(f"Class Name: {class_name}")
                new_text = element.get_text(strip=True)
                if new_text == '':
                    new_text = element.next_sibling
                    new_text = new_text.strip()
                print(f"Text: {new_text}")
                print('---')


    def run(self):
        class_names = input("Enter the class names, separated by commas: ").split(',')
        self.extract_multiple_classes(class_names)

# Example usage
url = input("Enter the website URL: ").strip()
scraper = WebScraper(url)
scraper.run()
