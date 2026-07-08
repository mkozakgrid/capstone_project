import unittest
from part2.task_read_write import read_write_file
import os

class TestReadWrite(unittest.TestCase):
    def test_read_write_file(self):
        expected_content = ""
        for i in range(19):
            with open(f"files/file{i+1}.txt", "r") as file:
                expected_content += file.read()
        read_write_file()
        with open("output.txt", "r") as file:
            actual_content = file.read()
        self.assertEqual(expected_content, actual_content)


if __name__ == "__main__":
    unittest.main()