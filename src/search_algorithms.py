import numpy as np 
def preprocess(text):
    """
    Basic preprocessing: Lowercase, tokenize (add stemming/lemmatization if desired).

    Args:
        text (str): The input text.

    Returns:
        list: A list of processed tokens.
    """
    tokens = text.lower().split()
    

    # Convert the list of tokens back into a string 
    return " ".join(tokens) 


def boolean_search(query, documents):
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
    for i, doc in enumerate(preprocessed_docs): # Iterate over documents
        if all(term in doc for term in preprocessed_query if term[0] != "-") and all(term not in doc for term in preprocessed_query if term[0] == "-"):
            relevant_docs.append(i)

    return relevant_docs

def create_term_document_matrix(documents):
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
    preprocessed_query = preprocess(query)
    print("Preprocessed query: ",preprocessed_query)
    preprocessed_docs = [preprocess(doc) for doc in documents]
    print("Preprocessed docs: ",preprocessed_docs)

    term_document_matrix = create_term_document_matrix(preprocessed_docs)
    print("Term document matrix: ",term_document_matrix)

   
    query_vector = np.array([term_document_matrix[term_index, :] for term_index, term in enumerate(preprocessed_query.split()) if term in term_document_matrix]) 
    print("Query vector: ",query_vector)
    if len(preprocessed_query.split()) == 0 or all(term not in term_document_matrix for term in preprocessed_query.split()): # Handle the case where the query is empty or has no terms in common
       similarities = [0 for _ in range(len(term_document_matrix.T))]  # Assign zero similarities for debugging purposes
    else:
      similarities = [calculate_cosine_similarity(query_vector, doc_vector) for doc_vector in term_document_matrix.T] 
    print("similarities: ",similarities)
    return list(zip(range(len(documents)), similarities)) 



def calculate_collection_frequencies(documents):
    collection_freq = {}
    for doc in documents:
        for term in doc:
            if term in collection_freq:
                collection_freq[term] += 1
            else:
                collection_freq[term] = 1
    return collection_freq

