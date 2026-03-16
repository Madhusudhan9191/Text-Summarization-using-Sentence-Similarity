# Text Summarizer

A Python-based text summarizer that uses sentence similarity and PageRank to rank and extract the most important sentences.

## Features
- Tokenizes and preprocesses sentences using stemming and lemmatization.
- Builds a similarity matrix based on cosine distance.
- Uses PageRank to identify the most relevant sentences.

## Installation
1. Clone the repository:
   ```bash
  git clone https://github.com/Madhusudhan9191/Text-Summarization-using-Sentence-Similarity.git
  cd Text-Summarization-using-Sentence-Similarity

Install required dependices

pip install -r requirements.txt


## How It Works

1. The input document is split into sentences.
2. Text preprocessing is applied (tokenization, stopword removal, stemming).
3. A sentence similarity matrix is built using cosine similarity.
4. A graph is created where sentences are nodes.
5. PageRank algorithm ranks sentences based on importance.
6. The top ranked sentences are selected as the final summary.
