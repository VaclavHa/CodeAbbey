DATA = """
8
6 10 67
1 4 95
16 1 29
8 17 94
15 7 32
26 2 37
10 0 78
1 19 35
"""


def get_numbers(data):
    numbers_list = []
    data = data.strip().split("\n")
    for row in data[1:]:
        numbers = row.split(" ")
        a, d, n = [int(number) for number in numbers]
        numbers_list.append((a, d, n))
    return numbers_list


def ar_prog(data):
    for a, d, n in get_numbers(data):
        sum_ap = (n / 2) * (2 * a + (n - 1) * d)
        print(int(sum_ap), " ")


if __name__ == '__main__':
    get_numbers(DATA)
    ar_prog(DATA)
