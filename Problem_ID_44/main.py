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


def dice_roll_double(data):
    dice_throws = []
    for data_line in data:
        num_1, num_2 = data_line[0], data_line[1]
        throw_1 = (num_1 % 6) + 1
        throw_2 = (num_2 % 6) + 1
        dice_roll = throw_1 + throw_2
        dice_throws.append(dice_roll)

    return dice_throws


if __name__ == '__main__':
    data_to_proceed = parse_data(INPUT)
    results = dice_roll_double(data_to_proceed)

    for number in results:
        print(number)
