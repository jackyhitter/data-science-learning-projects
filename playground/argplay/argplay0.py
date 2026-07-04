import sys 


if len(sys.argv) != 3:
    print("Usage: python app.py <name> <age>")
    exit()

name = sys.argv[1] if len(sys.argv) > 1 else "World"
age = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 0

print(f"Hello, {name}! You are {age} years old.")