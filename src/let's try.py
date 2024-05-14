import random

word_list_path = "fifth_document.txt"


def read_word_list(file_path):
    with open(file_path,'r') as file:
        words = file.read().lower()
        return words.split()

# Read the word list from the file
word_list = read_word_list(word_list_path)
def generate_random_words(word_list, num_words):
  """Generates a list of random words without duplicates, up to num_words."""
  random_words = []
  while len(random_words) < num_words:
    word = random.choice(word_list)
    random_words.append(word)
  return random_words

# Generate random documents with 100 words each
empty_documents = [[] for _ in range(4)]  # List of four empty lists
for document in empty_documents:
  document.extend(generate_random_words(word_list, 100))
file_names=['DOC1.txt','DOC2.txt','DOC3.txt','DOC4.txt']
for i, document in enumerate(empty_documents):
    file_name = file_names[i]
    with open(file_name, "w") as file:
      # Join list elements with newlines for text file format
      file.write("\n".join(document))

# Print the generated documents
for i, document in enumerate(empty_documents):
  print(f"Document {i+1}: {document}")

