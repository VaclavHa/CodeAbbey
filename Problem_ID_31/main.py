INPUT_DATA = "input.txt"


def get_and_parse_data(input_data: str):
    """
    Parse data to proceed with rotation
    :param input_data: file with lines of data
    :return: List of split data to number and string to rotate
    """
    parsed_data = list()
    with open(input_data, mode='r') as file:
        for line in file.readlines():
            parsed_line = line.strip().split()
            parsed_data.append((int(parsed_line[0]), parsed_line[1]))
    return parsed_data


def rotate_string(data: list):
    """
    Rotate string
    :param data: list of parsed data
    :return: list of rotated strings
    """
    rotated_strings = list()
    for steps, string in data:
        looped_string = ""
        if steps > 0:
            for letter in string[:steps]:
                looped_string += letter
            rotated_strings.append(string[steps:] + looped_string)
        if steps < 0:
            new_string = string[steps:]
            rotated_strings.append(new_string + (string[:(len(string) - abs(steps))]))
    return rotated_strings


if __name__ == '__main__':
    data_to_proceed = get_and_parse_data(INPUT_DATA)
    result = rotate_string(data_to_proceed)
    print(" ".join(result))
