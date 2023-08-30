#!/usr/bin/env python3

import sys


def factorize(num):
    factors = []
    for i in range(2, num):
        if num % i == 0:
            factors.append((i, num // i))
    return factors


def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                num = int(line.strip())
                factorizations = factorize(num)
                for p, q in factorizations:
                    print(f"{num}={p}*{q}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid number in the file.")
        sys.exit(1)


if __name__ == "__main__":
    main()
