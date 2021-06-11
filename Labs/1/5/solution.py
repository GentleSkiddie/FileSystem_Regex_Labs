import os
import datetime
import argparse


class Date(object):
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


# Simple check function whether the target date newer the date
def is_date_newer(target_date: Date, date: Date):
    if target_date.year > date.year:
        return True
    if target_date.year == date.year:
        if target_date.month > date.month:
            return True
        if target_date.month == date.month:
            if target_date.day > date.day:
                return True
    return False


# Function which returns the distributed weighted value for sorting in sorted function
def sort_time(date: tuple):
    return int(date[1].split()[0]) * 1 + int(date[1].split()[1]) * 1000 + int(date[1].split()[2]) * 100000


def walk(path, date, paths_to_files, is_newer=True, is_older=True, is_recursive=True):
    for filename in os.listdir(path):

        if os.path.isfile(os.path.join(path, filename)):

            file_path = os.path.join(path, filename).replace("\\", "/")
            date_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path) + 3600)
            # don't know why - time error while getting modify time: diff is 1 hour everywhere so adding 3600s
            target_date = Date(date_time.day, date_time.month, date_time.year)

            if is_newer:
                if is_date_newer(target_date, date):
                    paths_to_files.append(
                        (file_path, str(target_date.day) + " " + str(target_date.month) + " " + str(target_date.year)))
            else:
                if is_older and not is_date_newer(target_date, date):
                    paths_to_files.append(
                        (file_path, str(target_date.day) + " " + str(target_date.month) + " " + str(target_date.year)))

        path_to_file = os.path.join(path, filename)
        if os.path.isdir(path_to_file) and is_recursive:  # what if directory
            walk(path_to_file, date, paths_to_files, is_newer, is_older, is_recursive)  # going deeper
    return paths_to_files


def solve(directory, date, is_recursive=True, is_newer=True, is_sorted=True, is_older=True):
    date = Date(int(date.split()[0]), int(date.split()[1]), int(date.split()[2]))
    if is_sorted:
        return sorted(walk(directory, date, list(), is_newer, is_older, is_recursive), key=sort_time)
    return walk(directory, date, list(), is_newer, is_older, is_recursive)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("directory", help="Root directory")
    parser.add_argument("date", help="Date to search")
    parser.add_argument("-r", "--is_recursive", type=bool, default=True, help="Is search recursive")
    parser.add_argument("-g", "--is_newer", type=bool, default=True, help="Search for files newer than the argument")
    parser.add_argument("-l", "--is_older", type=bool, default=True, help="Search for files older than the argument")
    parser.add_argument("-s", "--is_sorted", type=bool, default=True, help="Are files sorted by date")

    args = parser.parse_args()

    print(solve(args.directory, args.date, args.is_recursive, args.is_newer, args.is_sorted, args.is_older))
