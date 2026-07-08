import string
import random

def generate_words(n: int):
    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k = random.randint(3, 10)))
        words.append(word)
    return words

def write_words(words: list):
    file1 = open("file1.txt", "w", encoding = "UTF-8")
    file2 = open("file2.txt", "w", encoding = "CP1252")

    for word in words:
        file1.write(word + "\n")
        file2.write(word + ", ")
    
    file1.close()
    file2.close()