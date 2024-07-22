INPUT_DATA = "input.txt"


def get_data(input_data):
    """
    Parse numbers to get individual floats
    :param input_data: str of numbers
    :return: parsed numbers
    """
    with open(input_data, mode="r") as file:
        data = file.read()
        parsed_data = [float(num) for num in data.split()]
    return parsed_data


def proceeded_data(numbers: list):
    """
    Proceed data to add number and adjacently numbers except first and last number in the list which remain the same
    :param numbers: list of parsed numbers
    :return: list of proceeded numbers
    """
    processed_numbers = []
    for i in range(1, len(numbers) - 1):
        avr = (numbers[i] + numbers[i - 1] + numbers[i + 1]) / 3
        processed_numbers.append(round(avr, 10))
    processed_numbers.insert(0, numbers[0])
    processed_numbers.append(numbers[-1])
    return processed_numbers


if __name__ == '__main__':
    numbers = get_data(INPUT_DATA)
    result = proceeded_data(numbers)
    print(result)
