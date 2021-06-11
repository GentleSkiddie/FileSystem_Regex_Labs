import re
import os
import argparse


def solve(file):
    file_path = os.path.join(os.getcwd(), file)
    pattern = r"^[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*" \
              r"@" \
              r"(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
    with open(file_path, encoding="utf8") as f:
        data = f.read().replace(" ", "\n")
        refs = re.findall(pattern, data, re.MULTILINE)
        if refs:
            return list(set(refs))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="Txt file with emails relative path")

    args = parser.parse_args()
    print(solve(args.file))
