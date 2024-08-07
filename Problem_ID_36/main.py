INPUT = "input.txt"


def parse_data(input_data):
    parsed_data = []
    with open(input_data, mode="r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip().split()
            test_cases = []
            for num in line:
                test_cases.append(int(num))
            parsed_data.append(test_cases)

    return parsed_data


def count_rate(data_to_process):
    list_of_counts = []
    for data in data_to_process:
        start_money, goal, bank_interest = data[0], data[1], data[2]

        money = start_money
        count = 0
        int_precent = bank_interest / 100

        while money < goal:
            money += money * int_precent
            count += 1
        list_of_counts.append(count)

    return list_of_counts


if __name__ == '__main__':
    processed_data = parse_data(INPUT)
    results = count_rate(processed_data)

    for result in results:
        print(result)
