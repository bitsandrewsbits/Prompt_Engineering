import requests
import re
from bs4 import BeautifulSoup
import json

article_URL = "https://blog.dzencode.com/ru/illyuziya-kachestva-vash-sayt-idealen-pozdravlyaem-vy-tolko-chto-sozhgli-byudzhet/"

article_metadata = {'url': article_URL, 'lang': '', 'date': '', 'topic': ''}

def main(URL: str):
    response = requests.get(URL)
    if response.status_code == 200:
        article_html = get_article_html(response)
        html_parser = BeautifulSoup(article_html, 'html.parser')
        article_metadata['lang'] = get_article_lang(response)
        article_metadata['date'] = get_request_date(response)
        article_metadata['topic'] = get_article_topic(html_parser)
        save_metadata(article_metadata)
        save_article_HTML_to_txt(article_html)
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

def save_metadata(metadata: dict):
    with open('metadata.json', 'w') as mdf:
        json.dump(metadata, mdf)

def save_article_HTML_to_txt(article_html):
    with open('article.txt', 'w') as article_f:
        article_f.write(article_html)

if __name__ == "__main__":
    main(article_URL)
