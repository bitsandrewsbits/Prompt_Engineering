# Data chunking for RAG
import json

preprocessed_article_text_file = 'cleaned_article.txt'
article_metadata_file = 'metadata.json'
chunks_JSONL_filename = 'rag_article.jsonl'

chunk_size_in_tokens = 512

def main(preprocessed_article_file: str, chunk_size_in_tokens: int, metadata_file: str, chunks_JSONL_file: str):
	preprocessed_article_text = get_preprocessed_article_text(preprocessed_article_file)
	article_tokens = get_article_tokens(preprocessed_article_text)
	metadata = get_metadata(metadata_file)
	chunked_data = get_chunked_data(article_tokens, chunk_size_in_tokens, metadata)
	save_chunks_into_JSONL(chunked_data, chunks_JSONL_file)

def get_preprocessed_article_text(filename: str):
	with open(filename, 'r') as prep_txt_f:
		preprocessed_article_text = prep_txt_f.read()
		return preprocessed_article_text

def get_article_tokens(article_text: str) -> list:
	return article_text.split(' ')

def get_chunked_data(article_tokens: list, chunk_size_in_tokens: int, metadata: dict):
	chunk_ID = 1
	chunked_data = []
	while len(article_tokens) != 0:
		chunk_metadata = metadata.copy()
		chunk_metadata['chunk_ID'] = chunk_ID
		chunk = {'chunk_tokens': [], 'metadata': []}
		chunk['metadata'] = chunk_metadata
		chunk['chunk_tokens'] = get_chunk(article_tokens, chunk_size_in_tokens)
		chunked_data.append(chunk)
		chunk_ID += 1
	return chunked_data

def get_chunk(article_tokens: list, chunk_size_in_tokens: int):
	if len(article_tokens) - chunk_size_in_tokens < chunk_size_in_tokens:
		chunk_size_in_tokens = len(article_tokens)
	return [article_tokens.pop(0) for _ in range(chunk_size_in_tokens)]

def get_metadata(metadata_file: str):
	with open(metadata_file, 'r') as metadata_f:
		return json.load(metadata_f)

def save_chunks_into_JSONL(chunks: list, JSONL_file: str):
	serialized_jsonl_chunks = '\n'.join([json.dumps(chunk) for chunk in chunks])
	with open(JSONL_file, 'w') as jsonl_f:
		jsonl_f.write(serialized_jsonl_chunks)

if __name__ == '__main__':
	main(preprocessed_article_text_file, 
		chunk_size_in_tokens, 
		article_metadata_file,
		chunks_JSONL_filename
	)