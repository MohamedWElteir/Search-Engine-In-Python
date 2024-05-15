import numpy as np


def calculate_cosine_similarity(vector1, vector2):
    """
    Calculates cosine similarity between two vectors.

    Args:
        vector1 (numpy.ndarray): The first vector.
        vector2 (numpy.ndarray): The second vector.

    Returns:
        float: The cosine similarity score (between 0 and 1).
    """
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))


def calculate_jaccard_similarity(set1, set2):
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

def calculate_document_similarity(doc1, doc2):
    """
    Calculates cosine similarity between two vectors.

    Args:
        doc1 (numpy.ndarray): The first vector.
        doc2 (numpy.ndarray): The second vector.

    Returns:
        float: The cosine similarity score (between 0 and 1).
    """
    return np.dot(doc1, doc2) / (np.linalg.norm(doc1) * np.linalg.norm(doc2))


# Example for debugging
if __name__ == "__main__":
    # For cosine similarity
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 1, 0])
    similarity = calculate_cosine_similarity(vector1, vector2) 
    print(f"Cosine similarity: {similarity:.4f}")

    # For Jaccard similarity  (assuming words are already preprocessed)
    doc1_terms = {"hello", "world", "search"}
    doc2_terms = {"search", "engine", "world"}
    similarity = calculate_jaccard_similarity(doc1_terms, doc2_terms) 
    print(f"Jaccard similarity: {similarity:.4f}")
