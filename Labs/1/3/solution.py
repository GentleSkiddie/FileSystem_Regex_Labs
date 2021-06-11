import os
import argparse


def walk(path, text, paths_to_files, depth=5, level=1, case_sensitive=True, is_recursive=True):
    for filename in os.listdir(path):
        path_to_file = os.path.join(path, filename)

        if os.path.isfile(path_to_file):
            with open(os.path.join(path, filename)) as file:

                file_text = file.readline()
                if not case_sensitive:
                    file_text.lower()
                    text.lower()

                if text in file_text:
                    file_path = os.path.relpath(os.path.join(path, filename)).split("\\")

                    for i in range(len(file_path) - level):
                        del file_path[0]  # deleting first directories from path to file

                    target_path = "."
                    for i in file_path:
                        target_path += ("/" + i)
                    paths_to_files.append(target_path)

        if os.path.isdir(path_to_file) and level < depth and is_recursive:  # what if directory
            walk(path_to_file, text, paths_to_files, depth, level + 1, case_sensitive, is_recursive)  # going deeper

    return paths_to_files


def solve(directory, text, is_recursive=True, depth=5, case_sensitive=True):
    return walk(directory, text, list(), depth, case_sensitive, is_recursive)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("directory", help="Root directory")
    parser.add_argument("text", help="Text to search")
    parser.add_argument("-r", "--is_recursive", type=bool, default=True, help="Is search recursive")
    parser.add_argument("-d", "--depth", type=int, default=5, help="Depth of search")
    parser.add_argument("-c", "--case_sensitive", type=bool, default=True, help="Whether to case-sensitive")

    args = parser.parse_args()

    print(solve(args.directory, args.text, args.is_recursive, args.depth, args.case_sensitive))
