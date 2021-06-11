import os
import argparse


def walk(path, file_type, paths_to_files, is_recursive=True, depth=5, level=1):
    for file in os.listdir(path):
        path_to_file = os.path.join(path, file)

        if os.path.isfile(path_to_file):
            if file.endswith(file_type):
                filename = file[:file.find(".")]
                paths_to_files.append(os.path.join(path, filename).replace("\\", "/"))

        if os.path.isdir(path_to_file) and level < depth and is_recursive:  # what if directory
            walk(path_to_file, file_type, paths_to_files, is_recursive, depth, level + 1)  # going deeper

    return paths_to_files


def solve(directory, file_type, is_recursive=True, depth=5):
    return walk(directory, file_type, list(), is_recursive, depth)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("directory", help="Root directory")
    parser.add_argument("file_type", help="File type to search")
    parser.add_argument("-r", "--is_recursive", type=bool, default=True, help="Is search recursive")
    parser.add_argument("-d", "--depth", type=int, default=5, help="Search depth")

    args = parser.parse_args()

    print(solve(args.directory, args.file_type, args.is_recursive, args.depth))
