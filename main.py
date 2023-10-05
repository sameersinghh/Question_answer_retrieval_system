!pip install -U sentence-transformers
from sentence_transformers import SentenceTransformer, util
import os
import json
import gzip
util.http_get('https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/datasets/simplewiki-2020-11-01.jsonl.gz', 'simplewiki-2020-11-01.jsonl.gz')
model = SentenceTransformer('nq-distilbert-base-v1')
passages = []
with gzip.open('simplewiki-2020-11-01.jsonl.gz', 'rt', encoding='utf8') as file:
  for line in file:
    data = json.loads(line.strip())
    # print(data)
    for paragraph in data['paragraphs']:
      passages.append([data['title'], paragraph])
    # break
len(passages)
from random import shuffle
shuffle(passages)
passages = passages[0:100_000]
corpus_embeddings = model.encode(passages, convert_to_tensor=True, show_progress_bar=True)
def get_answer(query):

  question_embedding = model.encode(query, convert_to_tensor=True)
  hits = util.semantic_search(question_embedding, corpus_embeddings, top_k=3)[0]

  print("Results:")
  for hit in hits:
    print(passages[hit['corpus_id']])
