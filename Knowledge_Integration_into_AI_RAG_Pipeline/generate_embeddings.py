# Embeddings Generations using 
#Sentence-BERT transformer pretrained model
import json
import pickle
from langchain_huggingface import HuggingFaceEmbeddings
from global_variables import *

EMBEDDINGS_MODEL = HuggingFaceEmbeddings(model_name = f"sentence-transformers/{SENTENCE_TRANSFORMER_MODEL_NAME}")

def main(chunks_file, embed_model, embed_vectors_filename):
    chunks = get_chunked_data(chunks_file)
    chunks_texts_embedding_vectors = get_chunks_texts_embed_vectors(embed_model, chunks)
    save_chunks_embedding_vectors(chunks_texts_embedding_vectors, embed_vectors_filename)

def get_chunked_data(chunks_file: str) -> list[dict]:
	loaded_chunked_data = []
	with open(chunks_file, 'r') as chunks_f:
		for line in chunks_f:
			loaded_chunked_data.append(json.loads(line))
	return loaded_chunked_data

def get_chunks_texts_embed_vectors(embed_model, chunks):
    chunks_texts = [chunk[CHUNK_DATA_TEXT_KEY] for chunk in chunks]
    return embed_model.embed_documents(chunks_texts)

def save_chunks_embedding_vectors(embed_vectors, filename: str):
    with open(filename, 'wb') as embed_vectors_f:
        pickle.dump(embed_vectors, embed_vectors_f)
    print(f'Embedding Vectors Saved into {filename}!')
    
if __name__ == '__main__':
	main(CHUNKS_JSONL_FILENAME,
		EMBEDDINGS_MODEL,
		EMBEDDING_VECTORS_FILENAME
	)