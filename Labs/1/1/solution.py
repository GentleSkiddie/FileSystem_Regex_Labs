import os
import argparse


def walk(path, file, depth=5, level=1, is_recursive=True):
    target_file = str()  # the file being searched for
    for filename in os.listdir(path):

        path_to_file = os.path.join(path, filename)

        if filename == file and os.path.isfile(path_to_file):
            target_file = os.path.join(path, filename)
            return target_file

        if os.path.isdir(path_to_file) and (level < depth) and is_recursive:  # what if directory
            target_file = walk(path_to_file, file, depth, level + 1)  # going into and returning file if exists there
            if target_file:
                return target_file

    return target_file


def solve(directory, file, is_recursive=True, depth=5):
    return walk(directory, file, depth, is_recursive).replace("\\", "/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("directory", help="Root directory")
    parser.add_argument("file", help="File to search")
    parser.add_argument("-r", "--is_recursive", type=bool, default=True, help="Is search recursive")
    parser.add_argument("-d", "--depth", type=int, default=5, help="Search depth")

    args = parser.parse_args()

    print(solve(args.directory, args.file, args.is_recursive, args.depth))
