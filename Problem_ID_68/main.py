INPUT = "input.txt"


def parse_data(input_data):
    parsed_data = []
    with open(input_data, mode="r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip().split()
            numbers = []
            for num in line:
                numbers.append(int(num))

            parsed_data.append(numbers)

    return parsed_data


def proceed_data(parsed_numbers):
    meeting_points = []
    for numbers in parsed_numbers:
        s, a, b = numbers[0], numbers[1], numbers[2]
        distance_a = (s * a) / (a + b)
        meeting_points.append(distance_a)

    return meeting_points


if __name__ == '__main__':
    data = parse_data(INPUT)
    results = proceed_data(data)
    for result in results:
        print(result)
