INPUT = "input.txt"


def get_and_parse_data(input):
    numbers = []
    with open(input, mode="r") as file:
        for num in file:
            numbers.append(int(num.strip()))

    return numbers


def fibonnaci(data):
    fibonacci_seq = [0, 1]

    while len(fibonacci_seq) <= 1000:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])

    fib_index_map = {value: index for index, value in enumerate(fibonacci_seq)}

    indicies = [fib_index_map[num] for num in data if num in fib_index_map]

    return indicies


if __name__ == '__main__':
    parsed_data = get_and_parse_data(INPUT)
    result = fibonnaci(parsed_data)

    for number in result:
        print(number)
