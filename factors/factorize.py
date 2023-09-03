import sys
import math


def factorize(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors


def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    # Get the input file name from the command-line argument
    input_file = sys.argv[1]

    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            # Read each line in the file
            for line in file:
                # Remove newline character and leading/trailing spaces
                number = line.strip()
                try:
                    # Convert the line to an integer
                    n = int(number)
                except ValueError:
                    print(f"Skipping invalid input: {number}")
                    continue

                # Find factors and print the result
                factors = factorize(n)
                print(f"{n}={'*'.join(map(str, factors))}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
        sys.exit(1)


if __name__ == "__main__":
    main()
