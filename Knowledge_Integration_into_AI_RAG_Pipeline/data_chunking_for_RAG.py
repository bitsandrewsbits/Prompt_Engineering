# Data chunking for RAG
preprocessed_article_text_file = 'cleaned_article.txt'
article_metadata_file = 'metadata.json'

chunk_size = 512

def main(preprocessed_article_file: str):
	preprocessed_article_text = get_preprocessed_article_text(preprocessed_article_file)
	article_tokens = get_article_tokens(preprocessed_article_text)
	print(len(article_tokens))

def get_preprocessed_article_text(filename: str):
	with open(filename, 'r') as prep_txt_f:
		preprocessed_article_text = prep_txt_f.read()
		return preprocessed_article_text

def get_article_tokens(article_text: str) -> list:
	return article_text.split(' ')

# TODO: think, how to getting chunk by chunk size. also add chunk ID
def get_chunk(chunk_size: int, current_chunk_ID: int):
	pass

if __name__ == '__main__':
	main(preprocessed_article_text_file)