DATA = """
15 93 160 195 226 185 0
3767 1469 1756 3406 3426 2198 66 0
4028 1059 567 434 1295 1876 2254 2371 1136 3235 0
49 213 167 73 141 96 154 3 41 238 112 154 29 0
9501 714 15125 15694 15340 7012 3812 1127 0
994 120 692 904 916 98 175 436 891 0
357 272 433 253 268 202 155 55 41 310 172 189 238 482 270 0
2965 3234 994 1053 3130 3637 2435 2730 917 845 1750 3805 1272 0
48 248 1 402 212 351 0
225 688 723 72 1010 0
2706 3695 1196 3158 2512 3674 137 3292 2429 1571 2271 0
1631 1872 2014 4033 3173 3073 2091 1888 1447 1325 407 3468 0
865 981 65 437 540 822 869 686 0
"""


def process_data(data):
    data = data.strip().split("\n")
    numbers = [[int(num) for num in row.split(" ")] for row in data]

    return numbers


def get_avg_of_arrs(numbers):
    result = []
    for each_list in numbers:
        summa = 0
        for each_number in each_list:
            summa += each_number
            avg = summa / (len(each_list) - 1)
        result.append(avg)
    return result


if __name__ == "__main__":
    numbers = process_data(DATA)
    result = get_avg_of_arrs(numbers)
    for num in result:
        print(round(num), end=" ")
