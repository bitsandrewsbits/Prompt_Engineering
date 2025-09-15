# article data cleaning and preprocessing
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import re

article_html_file = 'article.txt'
preprocessed_article_text_file = 'cleaned_article.txt'

article_language = 'russian'
stopwords = stopwords.words(article_language)

def main(article_filename: str):
	article_html = get_article_html(article_filename)
	article_without_html_tags = remove_html_tags(article_html)
	preprocessed_article_text = get_cleaned_preprocessed_article_text(article_without_html_tags)
	save_preprocessed_article_text(preprocessed_article_text)

def remove_html_tags(article_html: str):
	html_parser = BeautifulSoup(article_html, 'html.parser')
	only_article_text = html_parser.find('html').text
	return only_article_text

def get_cleaned_preprocessed_article_text(article_text: str):
	not_word_chars_digit_regex = r'[\W0-9]'
	lowered_article_text = article_text.lower()
	article_text_elements = re.split(not_word_chars_digit_regex, lowered_article_text)
	article_text_without_empty_strs_stopwords = [
		word for word in article_text_elements if word != '' and word not in stopwords
	]
	preprocessed_article_text = ' '.join(article_text_without_empty_strs_stopwords)
	return preprocessed_article_text

def get_article_html(article_filename: str):
	with open(article_filename, 'r') as article_f:
		article_html = article_f.read()
	return article_html

def save_preprocessed_article_text(preprocessed_text: str):
	with open(preprocessed_article_text_file, 'w') as prep_txt_f:
		prep_txt_f.write(preprocessed_text)

if __name__ == '__main__':
	main(article_html_file)