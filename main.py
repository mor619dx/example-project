from math_operations import divide_numbers
from string_operations import reverse_string
from utils import read_file

def main():
    # This will cause a ZeroDivisionError
    a = 10
    b = 0
    if b != 0:
        print(divide_numbers(a, b))
    else:
        print("Cannot divide by zero")

    # This will cause a TypeError
    print(reverse_string(None))

    # This will cause a FileNotFoundError
    print(read_file("non_existent_file.txt"))

if __name__ == "__main__":
    main()
