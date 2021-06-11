import argparse


def solve(number):
    if number == 0:
        return 0

    previous = current = 1

    for i in range(number - 2):
        [current, previous] = [current + previous, current]  # Switch values

    return current


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('number', type=int)

    args = parser.parse_args()

    print(solve(args.number))
