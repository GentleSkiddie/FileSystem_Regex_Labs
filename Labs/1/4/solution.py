import os
import argparse


def walk(path, size, paths_to_files, is_greater=True, is_less=True, is_recursive=True, is_sorted=True):
    for filename in os.listdir(path):

        if os.path.isfile(os.path.join(path, filename)):

            file_size = os.path.getsize(os.path.join(path, filename))
            file_path = os.path.join(path, filename).replace("\\", "/")

            if is_greater:
                if file_size > size:
                    paths_to_files.append((file_path, file_size))
            else:
                if is_less and file_size < size:
                    paths_to_files.append((file_path, file_size))

        path_to_file = os.path.join(path, filename)
        if os.path.isdir(path_to_file) and is_recursive:  # what if directory
            walk(path_to_file, size, paths_to_files, is_greater, is_less)  # going deeper
    if is_sorted:
        paths_to_files = sorted(paths_to_files, key=lambda x: x[1])
    return paths_to_files


def solve(directory, size, is_recursive=True, is_greater=True, is_sorted=True, is_less=True):
    return walk(directory, size, list(), is_greater, is_less, is_recursive, is_sorted)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("directory", help="Root directory")
    parser.add_argument("size", help="Text to search")
    parser.add_argument("-r", "--is_recursive", type=bool, default=True, help="Is search recursive")
    parser.add_argument("-g", "--is_greater", type=bool, default=True, help="Search for files larger than the argument")
    parser.add_argument("-l", "--is_less", type=bool, default=True, help="Search for files less than the argument")
    parser.add_argument("-s", "--is_sorted", type=bool, default=True, help="Sort files in ascending order of size")

    args = parser.parse_args()

    print(solve(args.directory, args.size, args.is_recursive, args.is_greater, args.is_sorted, args.is_less))
