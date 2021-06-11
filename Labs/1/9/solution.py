import argparse
import random


# Function returns max power of two of the number
def power_of_two(number):
    power = 0
    while number % 2 == 0:
        number >>= 1
        power += 1
    return power


def solve(number, k=3):
    if number < 2:
        return False
    if number == 3:
        return True
    r = power_of_two(number)
    s = number - 1
    for i in range(0, k):
        a = random.randrange(2, number - 1)
        x = pow(a, s, number)
        if x == 1 or x == number - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break
        else:
            return False
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('number', type=int)
    parser.add_argument('-r', "--rounds_number", type=int, default=3, help="rounds number")

    args = parser.parse_args()

    print(solve(args.number, args.rounds_number))
