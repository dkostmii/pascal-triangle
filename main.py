import sys
import os
from math import factorial

def main():
    n = 20

    if (len(sys.argv) > 1):
        try:
            n = int(sys.argv[1])
        except Exception:
            print(f"Expected argument to be integer. Got: {sys.argv[1]}")
            os._exit(1)

    results = []

    for i in range(n + 1):
        results.append(list(map(int, binomial(i))))

    max_digits = larges_number_lentgth(results[-1])

    lines = []
    for i in range(n + 1):
        lines.append(list_to_line(list(map(int, binomial(i))), max_digits))

    for line in lines:
        print(line.center(len(lines[-1])))


def larges_number_lentgth(numbers):
    if (not isinstance(numbers, list)):
        raise Exception("Expected numbers to be list")

    return max(list(map((lambda n: len(str(n))), numbers)))


def list_to_line(lst, places=None):
    if (not isinstance(lst, list)):
        raise Exception("Expected lst to be list")
    if (places is None):
        return ' '.join([str(value) for value in lst])

    return ' '.join([str(value).center(places) for value in lst])


def binomial(n):
    coeffs = []
    for i in range(n + 1):
        coeffs.append(factorial(n) / (factorial(i) * factorial(n - i)))

    return coeffs


if __name__ == "__main__":
    main()
