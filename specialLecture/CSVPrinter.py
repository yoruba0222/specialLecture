import csv


class CSVPrinter:
    def __init__(self, file_name: str) -> None:
        self.file_name: str = file_name
        
    def read(self) -> list:
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
            
        return lines