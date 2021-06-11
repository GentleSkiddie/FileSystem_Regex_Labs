import re
import argparse


def solve(string):
    pattern_ru = r"\+7(?:[\s]\d{3,4}[\s]|\(\d{3,4}\)|[\s]\(\d{3,4}\)[\s]|\d{3,4})\d{6,7}"
    pattern_ca = r"\+1(?:[\s]\d{3}[\s]|\(\d{3}\)|[\s]\(\d{3}\)[\s]|\d{3})\d{7}"
    pattern_cz = r"\+420(?:[\s]\d{2}[\s]|\(\d{2}\)|[\s]\(\d{2}\)[\s]|\d{2})\d{7}"
    pattern_fin = r"\+358(?:[\s]\d{2,3}[\s]|\(\d{2,3}\)|[\s]\(\d{2,3}\)[\s]|\d{3})\d{7,8}"
    patterns = r"|".join((pattern_ru, pattern_ca, pattern_cz, pattern_fin))
    match = re.search(patterns, string)
    return match is not None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("string", help="Phone number")

    args = parser.parse_args()

    print(solve(args.string))
