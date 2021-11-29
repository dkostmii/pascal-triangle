import sys
from math import factorial


def main():
    # default triangle height
    n = 20

    # parse argument
    if len(sys.argv) > 1:
        try:
            if int(sys.argv[1]) < 0:
                raise Exception(f"Expected n to be non-negative. Got: {sys.argv[1]}")

            n = int(sys.argv[1])
        except ValueError:
            print(f"Expected argument to be integer. Got: {sys.argv[1]}")
            sys.exit(1)
        except Exception as e:
            if (hasattr(e, 'message')):
                print(f"Error occurred: {e.message}")
            else:
                print(f"Error occurred: {e}")
            sys.exit(1)

    results = []

    # write values to results list
    for i in range(n + 1):
        results.append(list(map(int, binomial(i))))

    # get largest number digits count
    # to center all numbers
    max_digits = largest_number_length(results[-1])

    lines = []
    for i in range(n + 1):
        lines.append(list_to_line(list(map(int, binomial(i))), max_digits))

    # center lines with respect to last
    for line in lines:
        print(line.center(len(lines[-1])))


def largest_number_length(numbers):
    if not isinstance(numbers, list):
        raise Exception("Expected numbers to be list")

    # map number to it's digits count
    return max(list(map((lambda n: len(str(n))), numbers)))


def list_to_line(lst, places=None):
    if not isinstance(lst, list):
        raise Exception("Expected lst to be list")
    if places is None:
        return ' '.join([str(value) for value in lst])

    # center numbers in line with
    # for example 1 and max number 12345 result is: __1__
    # where _ is whitespace
    return ' '.join([str(value).center(places) for value in lst])


def binomial(n):
    coeffs = []
    for i in range(n + 1):
        # calculate the binomial coefficient
        # n choose k = n! / k! * (n - k)!
        coeffs.append(factorial(n) / (factorial(i) * factorial(n - i)))

    return coeffs


if __name__ == "__main__":
    main()
