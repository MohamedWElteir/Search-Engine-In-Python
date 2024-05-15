import random,os
from annotated_types import LowerCase
import nltk
from nltk.tokenize import word_tokenize


word_list_path = "wordList.txt"
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        content = word_tokenize(content)
    return content


# Read the word list from the file
word_list = read_file(word_list_path)

def content_to_list(folder_path):
    all_files_content=[]
    for filename in os.listdir("data"):
        if os.path.isfile(os.path.join(folder_path, filename)):    #check if file
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                file_contents=[line.strip() for line in file.readlines()]
            all_files_content.append(file_contents)
    return all_files_content


def generate():
    def generate_random_words(word_list, num_words):
        """Generates a list of random words, up to num_words."""
        random_words = []
        while len(random_words) < num_words:
            random_words.append(random.choice(word_list))
        return random_words

    # Generate random documents with 100 words each
    num = int(input("enter number of docs:"))
    folder_name="data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_names = []
    empty_documents = [[] for _ in range(num)]  # List of four empty lists
    for document in empty_documents:
        document.extend(generate_random_words(word_list, 100))
    for i in range(num):
        file_names.append(f"{folder_name}/DOC{i + 1}.txt")
    for i, document in enumerate(empty_documents):
        file_name = file_names[i]
        with open(file_name, "w") as file:
            file.write("\n".join(document))
    # Print the generated documents
    for i, document in enumerate(empty_documents):
        print(f"Document {i + 1}: {document}")


def take_inputes_from_users():
    num = int(input("enter the number of files : "))
    file_path = []
    content = []
    for i in range(num):
        file_path.append(input("enter the file destination : "))
        # Read the Files and divide them into tokens to compare them
        content.append(read_file(file_path[i]))
    print(content)
    print(len(content))
    return content


def start():
    user_choice = input("[*] Do U want to generate files randomly? : ")
    if user_choice.lower() == "yes" or user_choice.lower() == "y" or user_choice == 1:
        generate()
    else:
        take_inputes_from_users()



