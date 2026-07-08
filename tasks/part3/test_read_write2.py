import unittest
from part2.task_read_write2 import generate_words, write_words
import os

class TestReadWrite2(unittest.TestCase):
    def test_generate_words(self):
        words = generate_words(10)
        self.assertEqual(len(words), 10)
        write_words(words)
        with open("file1.txt", "r", encoding = "UTF-8") as file:
            file1_content = file.read()
        with open("file2.txt", "r", encoding = "CP1252") as file:
            file2_content = file.read()
        self.assertEqual(file1_content, file2_content)


if __name__ == "__main__":
    unittest.main()