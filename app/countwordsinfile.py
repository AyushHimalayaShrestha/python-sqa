# Count words in file
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            print("Total words:", len(words))
    except FileNotFoundError:
        print("File not found!")

count_words("sample.txt")
