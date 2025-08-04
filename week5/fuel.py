def main():
    """
    Get input fractions and print corresponding fuel status.
    """
    print("Fuel Gauge - Enter fractions (X/Y) or 'q' to quit")
    
    while True:
        fraction = input("Fraction: ").strip()
        
        if fraction.lower() == "q":
            break

        try:
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            

def convert(fraction: str) -> int:
    """Convert fraction string into percentage integer."""
    if "/" not in fraction:
        raise ValueError("Invalid format. Use X/Y format")
    
    parts = fraction.split("/")
    if len(parts) != 2:
        raise ValueError("Invalid format. Use X/Y format")
    
    x, y = parts
    try:
        x = int(x.strip())
        y = int(y.strip())
    except ValueError:
        raise ValueError("Numerator and denominator must be integers")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")
    
    return int(x / y * 100)
    

def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%" 


if __name__ == "__main__":
    main()
