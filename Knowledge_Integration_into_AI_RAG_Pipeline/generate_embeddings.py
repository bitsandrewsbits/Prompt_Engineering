# Embeddings Generations using 
#Sentence-BERT transformer pretrained model
import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
RAG_chunks_file = 'rag_article.jsonl'

def main(chunks_file: str):
	RAG_chunks_data = get_chunked_data(chunks_file)
	add_chunked_data_embeddings_to_chunks(RAG_chunks_data)
	print(RAG_chunks_data)

def get_chunked_data(chunks_file: str) -> list[dict]:
	loaded_chunked_data = []
	with open(chunks_file, 'r') as chunks_f:
		for line in chunks_f:
			loaded_chunked_data.append(json.loads(line))
	return loaded_chunked_data

def add_chunked_data_embeddings_to_chunks(chunks: list):
	for chunk in chunks:	
		chunk_embedding = model.encode(chunk['chunk_text'])
		chunk['embedding'] = chunk_embedding

if __name__ == '__main__':
	main(RAG_chunks_file)