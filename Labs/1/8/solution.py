import argparse


def euclid(x, y):
    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return max(x, y)


def solve(number):
    if number < 1000:
        for i in range(2, number // 2):
            if euclid(i, number) != 1:
                return False
    else:
        for i in range(number // 2 - 1000, number // 2):
            if euclid(i, number) != 1:
                return False
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('number', type=int)

    args = parser.parse_args()

    print(solve(args.number))
