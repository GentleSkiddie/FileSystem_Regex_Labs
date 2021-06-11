import re
import argparse


def solve(string):
    pattern = r"^(?:http|ftp)s?:\/\/\w(?:[\w\W]+\/?)+"
    match = re.match(pattern, string)
    return match is not None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="Html file relative path")

    args = parser.parse_args()
    print(solve(args.file))
