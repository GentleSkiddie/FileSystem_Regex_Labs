import argparse


def solve(number):
    if number == 0:
        return True

    previous = current = 1

    while number >= previous + current:
        if number == previous + current:
            return True
        [current, previous] = [current + previous, current]  # Switch values

    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('number', type=int)

    args = parser.parse_args()

    print(solve(args.number))
