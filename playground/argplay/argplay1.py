'''
=====================RAISING THE ERROR FOR INVALID ARGUMENTS========================
if args.arg2 <= args.arg1:
    parser.error(f"arg2 ({args.arg2}) must be greater than arg1 ({args.arg1})")

print("Arguments validated! arg2 is greater than arg1.")

if len(sys.argv) != 3:
    raise ValueError("Usage: python app.py <name> <age>")

---------------------------------------------------------------------------------
                  Creating own exception class :- 

class InvalidArgumentError(Exception):
    pass

if len(sys.argv) != 3:
    raise InvalidArgumentError(
        "Expected 2 arguments.\nUsage: python app.py <name> <age>"
    )

class InvalidArgumentError(Exception):
    pass

try:
    if len(sys.argv) != 3:
        raise InvalidArgumentError("Expected 2 arguments.")
except InvalidArgumentError as e:
    print(f"Error: {e}")
-------------------------------------------------------------------------------------
'''
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name", type = str, default = "User")
parser.add_argument("--age", type = int, default = 0, required = True)

args = parser.parse_args()

print(f"Hello, {args.name}! You are {args.age} years old.")

