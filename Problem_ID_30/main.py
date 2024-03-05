STRING = "turn why simple cocoa job stay coal make"


def reverse_string(string: str):
    rev_str = reversed(string)

    for char in rev_str:
        print("".join(char))


if __name__ == "__main__":
    reverse_string(STRING)
