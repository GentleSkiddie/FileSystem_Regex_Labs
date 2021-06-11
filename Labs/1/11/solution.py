import os
import argparse


def solve(file, is_sorted):
    for root, dirs, files in os.walk(os.getcwd()):
        for filename in files:
            if file in filename:
                with open(os.path.join(root, filename), 'r', encoding='utf-8') as f:
                    lines = list(set(f.readline().split(' ')))
                    if is_sorted:
                        lines.sort()
                    return lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="Name of file")
    parser.add_argument("-s", '--is_sorted', type=bool, default=True, help="Is list of strings sorted")

    args = parser.parse_args()

    print(solve(args.file, args.is_sorted))
