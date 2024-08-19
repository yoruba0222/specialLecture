import unittest

from specialLecture.CSVPrinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()

        self.assertEqual(3, len(line))
        
        for row in line:
            self.assertEqual(4, len(row))
            
        with self.assertRaises(FileNotFoundError):
            printer = CSVPrinter("fjweowfojafjwo")
            printer.read()


if __name__ == "__main__":
    unittest.main()