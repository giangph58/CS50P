import re


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    pattern = r"^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$"
    match = re.match(pattern, s)
    
    if not match:
        raise ValueError("Invalid format")
    
    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()
    
    # Convert to integers
    start_hour = int(start_hour)
    start_min = int(start_min) if start_min else 0
    end_hour = int(end_hour)
    end_min = int(end_min) if end_min else 0
    
    # Validate minutes
    if start_min >= 60 or end_min >= 60:
        raise ValueError("Invalid minutes")
    
    # Validate hours
    if start_hour < 1 or start_hour > 12 or end_hour < 1 or end_hour > 12:
        raise ValueError("Invalid hours")
    
    # Convert to 24-hour format
    if start_hour == 12:
        start_24 = 0 if start_period == "AM" else 12
    else:
        start_24 = start_hour if start_period == "AM" else start_hour + 12
    
    if end_hour == 12:
        end_24 = 0 if end_period == "AM" else 12
    else:
        end_24 = end_hour if end_period == "AM" else end_hour + 12
    
    # Format output
    return f"{start_24:02d}:{start_min:02d} to {end_24:02d}:{end_min:02d}"


if __name__ == "__main__":
    main()
