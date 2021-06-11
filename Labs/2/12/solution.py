import re
import os
import argparse


def solve(file, year, is_newer=True, is_older=False):
    file_path = os.path.join(os.getcwd(), file)
    pattern = r"^(?:3[0-1]|[1-2][0-9]|0[1-9])\/" \
              r"(?:1[0-2]|0[1-9])\/" \
              r"(?P<year>\d{4}) " \
              r"(?:2[0-4]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]$"
    dates = list()
    with open(file_path, encoding="utf8") as f:
        data = f.read().replace("; ", "\n")
        refs = re.finditer(pattern, data, re.MULTILINE)
        for i in refs:
            if is_newer and is_older:  # after and before the year
                if int(i.group("year")) > int(year) or int(i.group("year")) < int(year):
                    dates.append(i[0])
            if is_newer:  # after the year
                if int(i.group("year")) > int(year):
                    dates.append(i[0])
            else:  # before the year
                if int(i.group("year")) < int(year):
                    dates.append(i[0])
        if refs:
            return list(set(dates))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="Txt file with dates relative path")
    parser.add_argument("-y", "--year", type=int, default=2012, help="Year relative to which to search")
    parser.add_argument("-n", "--is_newer", type=bool, default=True, help="Print newer years")
    parser.add_argument("-o", "--is_older", type=bool, default=False, help="Print older years")

    args = parser.parse_args()

    print(solve(args.file, args.year, args.is_newer, args.is_older))
