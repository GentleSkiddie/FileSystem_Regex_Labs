import argparse


def solve(file, size, is_sorted):
    with open(file, 'r', encoding='utf-8') as f:
        lines = [line.split(",") for line in f.read().splitlines()]

    del lines[0]  # removing "login & password" string from list

    password_book = {k: v for k, v in lines}
    passwords = list(password_book.values())

    top_passwords = {}

    for target_password in passwords:
        top_passwords[target_password] = passwords.count(target_password)
    top_passwords = dict(sorted(top_passwords.items(), key=lambda x: x[1], reverse=True))

    res = {}
    i = 0
    for password in top_passwords:
        res[password] = top_passwords[password]
        i += 1
        if i == size:
            return res
    # Superfluous param: dictionary will always be sorted, as required by the task
    return is_sorted  # Just to satisfy the param usage. Never executed


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="Name of file")
    parser.add_argument("-n", "--size_of_dict", type=int, default=13, help="Dictionary size")
    parser.add_argument("-s", "--is_sorted", type=bool, default=True, help="Are passwords sorted")

    args = parser.parse_args()

    print(solve(args.file, args.size_of_dict, args.is_sorted))
