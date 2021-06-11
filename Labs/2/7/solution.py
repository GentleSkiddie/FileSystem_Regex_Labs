import re
import os
import argparse


def solve(file, language):
    file_path = os.path.join(os.getcwd(), file)
    pattern = str()
    if language == "ru":
        pattern = r"\+7(?:[\s]\d{3,4}[\s]|\(\d{3,4}\)|[\s]\(\d{3,4}\)[\s]|\d{3,4})\d{6,7}"
    elif language == "usa":
        pattern = r"\+1(?:[\s]\d{3}[\s]|\(\d{3}\)|[\s]\(\d{3}\)[\s]|\d{3})\d{7}"
    elif language == "bel":
        pattern = r"\+375(?:[\s]\d{2}[\s]|\(\d{2}\)|[\s]\(\d{2}\)[\s]|\d{2})\d{7}"
    elif language == "ch":
        pattern = r"\+86(?:[\s]\d{3}[\s]|\(\d{3}\)|[\s]\(\d{3}\)[\s]|\d{3})\d{8}"

    with open(file_path, encoding="utf8") as f:
        data = f.read()
        refs = re.findall(pattern, data)
        if refs:
            return list(set(refs))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="Txt file with phone numbers relative path")
    parser.add_argument("-l", "--lang", help="Country phone number format")

    args = parser.parse_args()

    print(solve(args.file, args.lang))
