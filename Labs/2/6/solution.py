import re
import argparse


def solve(string):
    pattern = r"^[a-zA-z0-9!#$%&'*+\/=?^_`{|}~()-]+" \
              r"(?:\.[a-zA-Z0-9!#$%&'*+\/=?^_`{|}~-]+)*" \
              r"@" \
              r"(?:[][a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.?)+" \
              r"[a-zA-Z0-9]?(?:[a-z0-9-]*[a-zA-Z0-9])?$"
    match = re.match(pattern, string)
    return match is not None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="Txt file with emails relative path")

    args = parser.parse_args()
    print(solve(args.file))
