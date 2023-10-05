# Question_answer_retrieval_system

You can input a query or a question. The script then uses semantic search to find relevant passages in Simple English Wikipedia (as it is smaller and fits better in RAM).
- https://huggingface.co/models?library=sentence-transformers&sort=downloads
- we use: `nq-distilbert-base-v1`

- It was trained on the Natural Questions dataset, a dataset with real questions from Google Search together with annotated data from Wikipedia providing the answer. For the passages, we encode the Wikipedia article tile together with the individual text passages.

- Train Dataset: https://ai.google.com/research/NaturalQuestions/dataset
- Test Dataset: http://sbert.net/datasets/

  #Downloades :
- https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/datasets/simplewiki-2020-11-01.jsonl.gz



https://github.com/sameersinghh/Question_answer_retrieval_system/assets/77580567/5ebf0e93-1f97-4269-b9b5-b3b9fb7bd92e

