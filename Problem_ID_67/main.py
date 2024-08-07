INPUT = "input.txt"


def get_and_parse_data(input):
    numbers = []
    with open(input, mode="r") as file:
        for num in file:
            numbers.append(int(num.strip()))

    return numbers


def fibonnaci(data):
    fib_sequence = [0, 1]

    while len(fib_sequence) <= 1000:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    fib_index_map = {value: index for index, value in enumerate(fib_sequence)}

    indices = [fib_index_map[num] for num in data if num in fib_index_map]

    return indices


if __name__ == '__main__':
    parsed_data = get_and_parse_data(INPUT)
    result = fibonnaci(parsed_data)

    for number in result:
        print(number)
