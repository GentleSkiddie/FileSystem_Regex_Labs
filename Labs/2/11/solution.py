import re
import argparse


def solve(string):
    string_list = list(string.replace("\t", " "))  # Replacing tabs due to their redundancy  with spaces

    word_indent_pattern = r"[\w][\s]{2,}[\w]"
    sent_indent_pattern = r"[\D]\.[\s]*[\D]"

    # Deleting extra spaces between words
    for i in re.finditer(word_indent_pattern, "".join(string_list)):
        for j in range(i.start() + 1, i.end() - 2):
            del string_list[i.start() + 1]

    # Deleting extra spaces at the end of sentence
    for i in re.finditer(sent_indent_pattern, "".join(string_list)):
        if i.end() - 3 > i.start() + 2:
            for j in range(i.start() + 2, i.end() - 3):
                del string_list[i.start() + 2]

    # Adding extra spaces after sentence
    for i in re.finditer(sent_indent_pattern, "".join(string_list)):
        if i.end() - 3 < i.start() + 2:
            for j in range(i.end() - 3, i.start() + 2):
                string_list.insert(i.start() + 2, " ")

    return "".join(string_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("string", help="Sentence to fix")

    args = parser.parse_args()

    print(solve(args.string))
