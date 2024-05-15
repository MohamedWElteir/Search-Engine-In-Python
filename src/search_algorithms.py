import imp
from annotated_types import LowerCase
import numpy as np
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize


def preprocess(text:str):
    """
    Basic preprocessing: Lowercase, tokenize, and apply stemming/lemmatization.

    Args:
        text (str): The input text.

    Returns:
        list: A list of processed tokens.
    """
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    processed_tokens = []

    for token in tokens:
        stemmed_token = stemmer.stem(token)
        lemmatized_token = lemmatizer.lemmatize(token)
        processed_tokens.append(lemmatized_token)
        string = ' '.join(processed_tokens)
    return string


def boolean_search(query:str, documents:list) -> list:
    """
    Implements Boolean search with AND, OR, NOT operators.

    Args:
        query (str): The user's search query.
        documents (list): A list of preprocessed document texts.

    Returns:
        list: Indices of relevant documents.
    """
   
    preprocessed_query = preprocess(query)
    preprocessed_docs = [preprocess(doc) for doc in documents]

    relevant_docs = []
    for i, doc in enumerate(preprocessed_docs): 
        if all(term in doc for term in preprocessed_query ):

            relevant_docs.append(1)
        else:
            relevant_docs.append(0)
    for i,bool in enumerate(relevant_docs):
        if bool ==0:
            print(f"document_{i + 1} -> non relevant")
        else:
            print(f"document_{i + 1} -> relevant")
            

    return relevant_docs



def create_term_document_matrix(documents:list):
    """
    Builds a term-document matrix

    Args:
        documents (list): A list of preprocessed document texts

    Returns:
        numpy.ndarray: The term-document matrix.
    """
    vocabulary = list(set([term for doc in documents for term in doc]))  
    matrix = np.zeros((len(documents), len(vocabulary)))

    for i, doc in enumerate(documents):
        for term in vocabulary: 
            matrix[i, vocabulary.index(term)] = doc.count(term)  # Simple term frequency

    return matrix

def calculate_cosine_similarity(query_vector, doc_vector):
    """
    Calculates the cosine similarity between a query vector and a document vector.

    Args:
        query_vector (numpy.ndarray): The query vector.
        doc_vector (numpy.ndarray): The document vector.

    Returns:
        float: The cosine similarity.
    """
    return np.dot(query_vector, doc_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(doc_vector))

def vector_space_search(query, documents):
    """
    Performs search using the Vector Space Model (with cosine similarity).

    Args:
        query (str): The user's search query.
        documents (list): A list of preprocessed document texts.

    Returns:
        list: A list of tuples (document index, similarity score).
    """
    preprocessed_query = [preprocess(query) for query in query]
    preprocessed_docs = [preprocess(doc) for doc in documents]

    term_document_matrix = create_term_document_matrix(preprocessed_docs)
    vocabulary = list(set([term for doc in preprocessed_docs for term in doc]))  # Get the unique terms
    query_vector = np.array([preprocessed_query.count(term) for term in vocabulary])
    similarities = [calculate_cosine_similarity(query_vector, doc_vector) for doc_vector in term_document_matrix]

    return [(i, similarity) for i, similarity in enumerate(similarities)]




def calculate_collection_frequencies(documents):
    collection_freq = {}
    for doc in documents:
        doc=doc.split()
        for term in doc:
            if term in collection_freq:
                collection_freq[term] += 1
            else:
                collection_freq[term] = 1
    return collection_freq


def statistical_search(query, documents):
    """
    Perform a statistical search by calculating a simple relevancy score.
    Args:
        query (str): The search query.
        documents (list of str): The list of documents.
    Returns:
        None
    """
    preprocessed_query = preprocess(query)
    print(preprocessed_query)
    preprocessed_docs = [preprocess(doc) for doc in documents]
    scores = []

    for doc in preprocessed_docs:
        score = 0.0
        for term in preprocessed_query:
            term_stats = doc.count(term) / len(doc)
            score += term_stats
        scores.append(score)

    indexed_scores = [(i + 1, value) for i, value in enumerate(scores)]

    # Sort the list of tuples based on the values in descending order
    sorted_scores = sorted(indexed_scores, key=lambda x: x[1], reverse=True)

    print("Relevancy will be:-")
    for index, value in sorted_scores:
        print(f"DOC{{{index}}} -> {value}")
