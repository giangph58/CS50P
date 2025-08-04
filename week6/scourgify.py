import sys
import csv


def main():
    """Return cleaned CSV"""
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    
    infile = sys.argv[1]
    outfile = sys.argv[2]

    if not infile.endswith(".csv") or not outfile.endswith(".csv"):
        sys.exit("Input and output must be CSV files")

    try:
        data = []
        with open(infile, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames

            if not headers or headers != ["name", "house"]:
                sys.exit(f"Invalid CSV format. Expected headers: ['name', 'house'], got: {headers}")
            
            for _, row in enumerate(reader, start=2):
                last, first = row["name"].split(",")
                data.append({"first": first.strip(), "last": last.strip(), "house": row["house"]})
        
        with open(outfile, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(data)
            
            
    except FileNotFoundError:
        sys.exit(f"Could not read {infile}")


if __name__ == "__main__":
    main()

