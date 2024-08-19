import sys
sys.path.append("../")

import unittest

from specialLecture import CSVPrinter


class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(4, len(line))


if __name__ == "__main__":
    unittest.main()