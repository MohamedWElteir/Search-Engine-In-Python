from pydoc import doc
import numpy as np


def calculate_cosine_similarity(query, document):
    """
    Calculates cosine similarity between two vectors.

    Args:
        vector1 (numpy.ndarray): The first vector.
        vector2 (numpy.ndarray): The second vector.

    Returns:
        float: The cosine similarity score (between 0 and 1).
    """
    return np.dot(query, document) / (np.linalg.norm(query) * np.linalg.norm(document))


def calculate_jaccard_similarity(set1, set2)-> float:
    """
    Calculates Jaccard similarity between two sets of terms.

    Args:
        set1 (set): The first set of terms.
        set2 (set): The second set of terms.

    Returns:
        float: The Jaccard similarity score (between 0 and 1).
    """
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return float(intersection) / union 

import numpy as np

def calculate_document_similarity(query, document):
    """
    Calculates the similarity between a query and a document.

    Args:
        query (str): The query text.
        document (str): The document text.

    Returns:
        float: The similarity score (between 0 and 1).
    """
    query_vector = convert_document_to_vector(query)
    document_vector = convert_document_to_vector(document)
    
    # Make sure both vectors have the same length
    max_length = max(len(query_vector), len(document_vector))
    query_vector = np.pad(query_vector, (0, max_length - len(query_vector)), mode='constant')
    document_vector = np.pad(document_vector, (0, max_length - len(document_vector)), mode='constant')
    
    print(f"Query Vector: {query_vector}")
    print(f"Document Vector: {document_vector}")

    return calculate_cosine_similarity(query_vector, document_vector)


def convert_document_to_vector(document):
    """
    Converts a document to a vector representation.

    Args:
        document (str): The document text.

    Returns:
        numpy.ndarray: The document vector.
    """
    print(f"Document: {document}")
    words = document.split()
    unique_words = set(words)
    vector = np.array([words.count(word) for word in unique_words])
    return vector


# Example for debugging
if __name__ == "__main__":
    # For cosine similarity
    vector1 = np.array([1, 0, 1])
    vector2 = np.array([1, 0, 1])
    similarity = calculate_cosine_similarity(vector1, vector2) 
    print(f"Cosine similarity: {similarity:.4f}")

    # For Jaccard similarity  (assuming words are already preprocessed)
    doc1_terms = {"hello", "world", "search"}
    doc2_terms = {"search", "engine", "world"}
    similarity = calculate_jaccard_similarity(doc1_terms, doc2_terms) 
    print(f"Jaccard similarity: {similarity:.4f}")
