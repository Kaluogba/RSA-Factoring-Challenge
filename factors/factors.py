#!/usr/bin/env python3

import sys

def factors(n):
    factors_list = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors_list.append(i)
    if n > 1:
        factors_list.append(n)
    return factors_list

def factorize_and_print(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                n = int(line)
                factorization = factors(n)
                factorization_str = '*'.join(map(str, factorization))
                print(f"{n}={factorization_str}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("Invalid input in the file. All lines should contain natural numbers greater than 1.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    factorize_and_print(filename)
