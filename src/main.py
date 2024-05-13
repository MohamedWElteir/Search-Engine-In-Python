from data_generator import generate_random_document
from search_algorithms import preprocess, boolean_search, vector_space_search, calculate_collection_frequencies 
from similarity import calculate_cosine_similarity, calculate_jaccard_similarity, calculate_document_similarity
from ranking import query_likelihood_model, jelinek_mercer_smoothing
from evaluation import calculate_precision, calculate_recall, calculate_f1_measure, calculate_rank_power

# --- Data Generation ---
NUM_DOCUMENTS = 4
documents = [generate_random_document(save_to_file=True) for _ in range(NUM_DOCUMENTS)]
print("Documents generated:")
for i, doc in enumerate(documents):
    print(f"Document {i+1}: {doc}")

# Preprocess documents 
preprocessed_docs = [preprocess(doc) for doc in documents]  

# --- User Input ---
while True:
    query = input("Enter your search query (or type 'exit'): ")
    if query.lower() == "exit":
        break

    # --- Search Algorithms --- 
    boolean_results = boolean_search(query, preprocessed_docs)  
    vsm_results = vector_space_search(query, preprocessed_docs)

    # --- Ranking ---
    collection_freq = calculate_collection_frequencies(preprocessed_docs) 
    vsm_results_ranked = sorted(vsm_results, key=lambda x: jelinek_mercer_smoothing(preprocess(query), preprocessed_docs[x[0]], collection_freq), reverse=True)
    print("Collection Frequencies:", collection_freq)
    print("VSM Results Ranked:", vsm_results_ranked)

    # --- Relevance Feedback ---
    threshold = 0.6  
    relevant_docs = [i for i, doc in enumerate(preprocessed_docs) if calculate_document_similarity(preprocess(query), doc) >= threshold]
    print("Relevant Documents:", relevant_docs)

    # --- Evaluation --- 
    precision = calculate_precision(relevant_docs, [doc_index for doc_index, _ in vsm_results_ranked])  
    recall = calculate_recall(relevant_docs, [doc_index for doc_index, _ in vsm_results_ranked])  # Add recall
    f1 = calculate_f1_measure(precision, recall)
    rank_power = calculate_rank_power(relevant_docs, [doc_index for doc_index, _ in vsm_results_ranked])  # Add Rank Power

    # --- Print Results --- 
    print("Boolean Search Results:", boolean_results)  
    print("Vector Space Model Results:")
    for doc_index, similarity in vsm_results_ranked:
        print(f"Document {doc_index + 1} - Similarity: {similarity:.4f}")

    print(f"Precision:  {precision:.4f}") 
    print(f"Recall: {recall:.4f}")
    print(f"F1 Measure: {f1:.4f}")
    print(f"Rank Power: {rank_power:.4f}") 
    print("Updated")
