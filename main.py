from utils.text_processing import preprocess_text, build_similarity_matrix
import networkx as nx
from nltk.corpus import stopwords

def read_article(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    sentences = [sentence.split(" ") for sentence in text.split(". ") if sentence]
    return sentences

def generate_summary(file_name, top_n=5):
    stop_words = stopwords.words("english")
    sentences = read_article(file_name)
    processed_sentences = preprocess_text(sentences, stop_words)

    # Step 2 - Generate similarity matrix
    similarity_matrix = build_similarity_matrix(processed_sentences, stop_words)

    # Step 3 - Rank sentences
    sentence_similarity_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Extract top sentences
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summarize_text = [" ".join(ranked_sentences[i][1]) for i in range(top_n)]

    # Output summarized text
    print("\n".join(summarize_text))

if __name__ == "__main__":
    generate_summary("data/fb.txt", 2)
