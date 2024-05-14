import numpy as np


def query_likelihood_model(query_terms, document, collection_freq=None):
    """
    Calculates the probability of a query according to the Query Likelihood Model

    Args:
        query_terms (list): List of terms in the query.
        document (list): List of terms in the document.
        collection_freq (dict): Optional. Pre-calculated term frequencies in the whole collection 

    Returns:
        float: The query likelihood score.
    """
    score = 1.0
    if collection_freq:
        for term in query_terms:
            term_doc_freq = document.count(term)
            term_collection_freq = collection_freq.get(term, 0)
            score *= (term_doc_freq + 1.0) / (len(document) + term_collection_freq)
    else:
        # Variant without collection statistics
        for term in query_terms:
            term_doc_freq = document.count(term)
            score *= term_doc_freq / len(document)

    return score


def jelinek_mercer_smoothing(query_terms, document, collection_freq, lambda_param=0.5):
    """
    Implements Jelinek-Mercer smoothing for language modeling.

    Args:
        query_terms (list): List of terms in the query.
        document (list): List of terms in the document.
        collection_freq (dict): Term frequencies in the collection.
        lambda_param (float): Smoothing parameter. Defaults to 0.5.

    Returns:
        float: The Jelinek-Mercer smoothed probability.
    """
    score = 1.0

    for term in query_terms:
        term_doc_freq = document.count(term)
        term_collection_freq = collection_freq.get(term, 0)
        p_jm = ((1-lambda_param) * term_doc_freq / len(document)) + \
               (lambda_param * term_collection_freq / sum(collection_freq.values()))
        score *= p_jm

    return score



