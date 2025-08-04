import sys


def main():
    """Count lines of code for a Python script"""
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    
    filename = sys.argv[1]
    
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    
    try:
        with open(filename, "r") as file:
            code_count = sum(1 for line in file if is_code(line))
            print(code_count)
    except FileNotFoundError:
        sys.exit("File does not exit")
        
        
def is_code(line: str) -> bool:
    """
    Determine if a line contains actual code (not comments or empty lines 
    """

    stripped = line.strip()

    if not stripped:
        return False
    # if stripped.startswith("#"):
    #     return False
    # if stripped.startswith('"""') or stripped.startswith("'''"):
    #     return False
    if stripped.startswith(("#", '"""', "'''")):
        return False
    return True


if __name__ == "__main__":
    main()
