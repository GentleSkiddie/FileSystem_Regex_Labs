import re
import os
import argparse


def solve(file):
    file_path = os.path.join(os.getcwd(), file)
    pattern = r"(https?:\/\/(?:[^\"]*title[^\"<]+)?[^\"\'<) ]+)"
    with open(file_path, encoding="utf8") as f:
        data = f.read().replace("\n", " ")
        refs = re.findall(pattern, data)
        if refs:
            return list(set(refs))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="Html file relative path")

    args = parser.parse_args()
    print(solve(args.file))
