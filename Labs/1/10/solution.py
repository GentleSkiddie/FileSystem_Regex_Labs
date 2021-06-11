import argparse


def solve(number):
    result = number

    i = 2
    while i * i <= number:
        if number % i == 0:
            while number % i == 0:
                number //= i
            result -= result // i
        else:
            i += 1

    if number > 1:
        result -= result // number

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('number', type=int)

    args = parser.parse_args()

    print(solve(args.number))
