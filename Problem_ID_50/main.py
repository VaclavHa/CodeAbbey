from typing import List

TEST_DATA = "input.txt"


def get_and_parse_data(input_data: str):
    """
    Load data from file and parse them.
    
    :param input_data: input data read from a file
    :return: list of parsed strings to be checked
    """
    replace_char = " -,./;'"
    parsed_strings = list()
    with open(input_data, mode='r') as f:
        for line in f.readlines():
            parsed_line = line.lower().strip()
            for letter in replace_char:
                parsed_line = parsed_line.replace(letter, "")
            parsed_strings.append(parsed_line)
    return parsed_strings


def check_for_palindrome(strings_to_check: List[str]):
    """
    Compare strings for palindromes.
    :param strings_to_check: list of parsed strings
    :return: list of strings of Y and N
    """
    results: list[str] = list()
    for s in strings_to_check:
        if s == s[::-1]:
            results.append("Y")
        else:
            results.append("N")
    return results


if __name__ == '__main__':
    strings = get_and_parse_data(TEST_DATA)
    result = check_for_palindrome(strings)
    print(" ".join(result))
