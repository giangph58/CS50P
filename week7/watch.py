import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str | None:
    match = re.search(r'src="([^"]*youtube[^"]*)"', s)
    if not match:
        return None
    
    url = match.group(1)
    
    path = re.search(r'([^/]+)$', url)
    if not path:
        return None

    return f"https://youtu.be/{path.group(1)}"
    
if __name__ == "__main__":
    main()
