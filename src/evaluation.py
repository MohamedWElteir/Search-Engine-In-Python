def calculate_precision(relevant, retrieved):
  """
  Calculates precision: Ratio of retrieved documents that are relevant.

  Args:
      relevant (list): List of indices of relevant documents.
      retrieved (list): List of indices of retrieved documents.

  Returns:
      float: The precision score.
  """
  if not retrieved:
    return 0  # Handle division by zero
  return len([doc for doc in retrieved if doc in relevant]) / len(retrieved)

def calculate_recall(relevant, retrieved):
  """
  Calculates recall: Ratio of relevant documents that are retrieved.

  Args:
      relevant (list): List of indices of relevant documents.
      retrieved (list): List of indices of retrieved documents.

  Returns:
      float: The recall score.
  """
  if not relevant:
    return 0  # Handle division by zero
  return len([doc for doc in retrieved if doc in relevant]) / len(relevant)

def calculate_f1_measure(precision, recall):
  """
  Calculates F1 measure: Harmonic mean of precision and recall.

  Args:
      precision (float): The precision score.
      recall (float): The recall score.

  Returns:
      float: The F1 measure score.
  """
  if precision + recall == 0:
    return 0  # Handle division by zero
  return 2 * (precision * recall) / (precision + recall)

def calculate_rank_power(relevant):
  """
  Calculates Rank Power: Measures the goodness of ranking based on relevant document positions.

  Args:
      relevant (list): List of indices of relevant documents.

  Returns:
      float: The Rank Power score.
  """
  if not relevant:
    return 0  # Handle no relevant documents

  return sum(relevant) / len(relevant)**2

# Example for debugging
if __name__ == "__main__":
  relevant_docs = [0, 2, 3]
  retrieved_docs = [1, 0, 3, 2]

  precision = calculate_precision(relevant_docs, retrieved_docs)
  recall = calculate_recall(relevant_docs, retrieved_docs)
  f1 = calculate_f1_measure(precision, recall)
  rank_power = calculate_rank_power(relevant_docs, retrieved_docs)

  print(f"Precision: {precision:.4f}")
  print(f"Recall: {recall:.4f}")
  print(f"F1 Measure: {f1:.4f}")
  print(f"Rank Power: {rank_power:.4f}")
