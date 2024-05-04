import random
import string
import os

def generate_random_document(doc_length=100, save_to_file=False, data_dir="data"):
    """
    Generates a random document of specified length.

    Args:
        doc_length (int): Desired length of the document (in characters). Defaults to 100.
        save_to_file (bool): If True, saves the document to a file in the 'data' directory. Defaults to False.
        data_dir (str): The directory where documents should be saved. Defaults to "data".

    Returns:
        str: The generated document content.
    """

    content = "".join(random.choice(string.ascii_lowercase) for _ in range(doc_length))

    if save_to_file:
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)  # Create the 'data' directory if it doesn't exist

        doc_name = f"document_{len(os.listdir(data_dir)) + 1}.txt"  # Auto-generate filename
        file_path = os.path.join(data_dir, doc_name)

        with open(file_path, "w") as f:
            f.write(content)

    return content
