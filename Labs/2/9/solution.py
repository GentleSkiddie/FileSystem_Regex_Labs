import re
import os
import argparse


def solve(file):
    file_path = os.path.join(os.getcwd(), file)
    pattern = r"^(?:" \
              r"\b(?:(?:[2](?:[0-4][0-9]|[5][0-5])|[1]?[0-9]?[0-9])|" \
              r"(?:(?:03(?:[0-6][0-7]|[7][0-7]))|(?:0[0-2][0-7][0-7]))|(?:0)[xX][0-9A-F]{2})\." \
              r"\b(?:(?:[2](?:[0-4][0-9]|[5][0-5])|[1]?[0-9]?[0-9])|" \
              r"(?:(?:03(?:[0-6][0-7]|[7][0-7]))|(?:0[0-2][0-7][0-7]))|(?:0)[xX][0-9A-F]{2})\." \
              r"\b(?:(?:[2](?:[0-4][0-9]|[5][0-5])|[1]?[0-9]?[0-9])|" \
              r"(?:(?:03(?:[0-6][0-7]|[7][0-7]))|(?:0[0-2][0-7][0-7]))|(?:0)[xX][0-9A-F]{2})\." \
              r"\b(?:(?:[2](?:[0-4][0-9]|[5][0-5])|[1]?[0-9]?[0-9])|" \
              r"(?:(?:03(?:[0-6][0-7]|[7][0-7]))|(?:0[0-2][0-7][0-7]))|(?:0)[xX][0-9A-F]{2})\b" \
              r")$|" \
              r"^(?:[2-9][5-9][6-9]|\d{4,9}|[4][1-2][1-9][1-4][1-9][1-6][1-7][1-2][1-9][1-5]|[1-3]\d{9})$|" \
              r"^(?:0[xX][0-9A-F]{8})$|^(?:0[0-3][0-7]{10})$"
    with open(file_path, encoding="utf8") as f:
        data = f.read().replace(", ", "\n")
        refs = re.findall(pattern, data, re.MULTILINE)
        if refs:
            return list(set(refs))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="Txt file with IPv4 addresses relative path")

    args = parser.parse_args()

    print(solve(args.file))
