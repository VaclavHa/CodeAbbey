INPUT = "input.txt"


def get_and_parse_input_data(input_data):
    parsed_data = []
    with open(input_data, mode='r') as file:
        for line in file:
            number, steps = map(int, line.split())
            parsed_data.append((number, steps))
    return parsed_data


def find_square(data):
    results_data = []
    for number, step in data:
        approx = 1
        for _ in range(step):
            d = number / approx
            approx = (approx + d) / 2
        results_data.append(round(approx, 12))
    return results_data


if __name__ == '__main__':
    data_to_proceed = get_and_parse_input_data(INPUT)
    results = find_square(data_to_proceed)
    for result in results:
        print(result)
