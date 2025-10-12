# Data chunking for RAG
import json
from global_variables import *

def main(preprocessed_article_file: str, chunk_size_in_tokens: int, metadata_file: str, chunks_JSONL_file: str):
    preprocessed_article_text = get_preprocessed_article_text(preprocessed_article_file)
    article_words = get_article_words(preprocessed_article_text)
    chunks_texts = get_chunks_texts(article_words, chunk_size_in_tokens)
    metadata = get_metadata(metadata_file)
    chunked_data = get_chunked_data(chunks_texts, metadata)
    save_chunks_into_JSONL(chunked_data, chunks_JSONL_file)

def get_preprocessed_article_text(filename: str):
	with open(filename, 'r') as prep_txt_f:
		preprocessed_article_text = prep_txt_f.read()
		return preprocessed_article_text

def get_article_words(article_text: str) -> list:
	return article_text.split(' ')

def get_chunked_data(chunks_texts: list[str], metadata: dict):
    current_chunk_ID = 1
    chunked_data = []
    for (chunk_ID, chunk_text) in enumerate(chunks_texts, current_chunk_ID):
        chunk_metadata = metadata.copy()
        chunk_metadata[CHUNK_METADATA_ID_KEY] = chunk_ID
        chunk = {CHUNK_DATA_TEXT_KEY: '', CHUNK_DATA_METADATA_KEY: chunk_metadata}
        chunk[CHUNK_DATA_TEXT_KEY] = chunk_text
        chunked_data.append(chunk)
    return chunked_data

def get_chunks_texts(article_words: list, words_symbols_amount_for_chunks: int):
    chunks_texts = []
    while len(article_words) != 0:
        chunk_words_remained_article_words = get_chunk_words(article_words, words_symbols_amount_for_chunks)
        chunks_texts.append(' '.join(chunk_words_remained_article_words['chunk_words']))
        article_words = chunk_words_remained_article_words['remained_article_words']
    return chunks_texts
        
def get_chunk_words(article_words: list, words_symbols_amount_for_chunks: int):
    chunk_words = []
    while len(''.join(chunk_words)) < words_symbols_amount_for_chunks:
        if len(''.join(article_words)) - words_symbols_amount_for_chunks < words_symbols_amount_for_chunks:
            chunk_words = article_words
            return {'chunk_words': chunk_words, 'remained_article_words': []}
        chunk_words.append(article_words.pop(0))
    return {'chunk_words': chunk_words, 'remained_article_words': article_words}

def get_metadata(metadata_file: str):
	with open(metadata_file, 'r') as metadata_f:
		return json.load(metadata_f)

def save_chunks_into_JSONL(chunks: list, JSONL_file: str):
	serialized_jsonl_chunks = '\n'.join([json.dumps(chunk) for chunk in chunks])
	with open(JSONL_file, 'w') as jsonl_f:
		jsonl_f.write(serialized_jsonl_chunks)

if __name__ == '__main__':
	main(PREPROCESSED_ARTICLE_TEXT_FILENAME,
		CHUNK_SIZE_IN_TOKENS,
		ARTICLE_METADATA_FILENAME,
		CHUNKS_JSONL_FILENAME
	)