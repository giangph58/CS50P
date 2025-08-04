import sys
from tabulate import tabulate
import csv


def main():
    """Output CSV table formatted as ASCII art"""
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    
    filename = sys.argv[1]
    
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")
    
    table = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames

            if not headers:
                sys.exit("Error: CSV file has no headers or is empty")
                
            for row in reader:
                table.append(list(row.values()))
        
        print(tabulate(table, headers=headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exit")

if __name__ == "__main__":
    main()