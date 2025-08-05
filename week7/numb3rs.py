import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    match = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if match is None:
        return False
    
    for i in range(1, 5):
        octet_str = match.group(i)
        
        if len(octet_str) > 1 and octet_str[0] == "0":
            return False
        
        if int(octet_str) > 255 or int(octet_str) < 0:
            return False
        
    return True
    

if __name__ == "__main__":
    main()
