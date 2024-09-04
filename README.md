# Basic Search Engine in Python
TThis is a basic search engine developed in Python as part of the coursework for CS 3404 (Information Retrieval) at Alexandria University. The project leverages the Natural Language Toolkit (NLTK) library to implement core concepts of information retrieval, such as tokenization, stemming, and stop-word removal. It utilizes an inverted index data structure to efficiently map words to their corresponding document IDs and supports searching for documents containing specific words or combinations thereof.

The search engine ranks documents based on relevance using well-known algorithms such as Term Frequency-Inverse Document Frequency (TF-IDF) and cosine similarity. Additionally, it employs the F-Measure to provide an optimal balance between precision and recall. While simple, this project serves as a robust foundation for building more advanced search engines.
## How to use
1. Clone the repository
2. Run the `main.py` file
3. Enter the search query
4. The search engine will return the relevant documents based on the query

## Requirements
- Python 3
- NLTK library
- Numpy library

## Files
1. `data_generator.py`: This file is used to generate the sample data for the search engine. It creates a set of documents and stores them in a file.
2. `evaluation.py`: This file contains the evaluation metrics used to evaluate the search engine performance.
3. `main.py`: This is the main file that contains the search engine implementation. It reads the documents from the file, builds the inverted index, and performs the search based on the query.
4. `ranking.py`: This file contains the ranking algorithms used to rank the documents based on the query.
5. `search_algorithms.py`: This file contains the search algorithms used to search for documents based on the query.
6. `similarity.py`: This file contains the similarity algorithms used to calculate the similarity between the query and the documents.

## References
- [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/information-retrieval-book.html)
- [NLTK library](https://www.nltk.org/)
- [Numpy library](https://numpy.org/)
- [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
- [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [F-Measure](https://en.wikipedia.org/wiki/F-score)


