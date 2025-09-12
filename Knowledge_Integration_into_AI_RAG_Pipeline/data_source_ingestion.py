import requests
import re
from bs4 import BeautifulSoup

article_URL = "https://blog.dzencode.com/ru/illyuziya-kachestva-vash-sayt-idealen-pozdravlyaem-vy-tolko-chto-sozhgli-byudzhet/"

article_metadata = {'url': article_URL, 'lang': '', 'date': '', 'topic': ''}

def main(URL: str):
    response = requests.get(URL)
    if response.status_code == 200:
        article_html_page = get_article_html(response)
        html_parser = BeautifulSoup(article_html_page, 'html.parser')
        article_metadata['lang'] = get_article_lang(response)
        article_metadata['date'] = get_request_date(response)
        article_metadata['topic'] = get_article_topic(html_parser)
        print(article_metadata)
    else:
        print(f"Error fetching data from API. Status code: {response.status_code}")
        print(f"Response:", response.text)

def get_article_lang(response):
    cookie_str = response.headers['Set-Cookie']
    lang_regex = re.compile(r"(USER_LANG=)([a-zA-Z]*);")
    lang_match_obj = lang_regex.search(cookie_str)
    lang = lang_match_obj.group(2)
    return lang

def get_request_date(response):
    return response.headers['Date']

def get_article_topic(html_parser):
    topic = html_parser.find('title').text
    return topic

def get_article_html(response):
    return response.text
    
if __name__ == "__main__":
    main(article_URL)