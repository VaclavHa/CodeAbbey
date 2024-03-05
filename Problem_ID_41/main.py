DATA = """
22
991 18 1000
808 426 818
976 1013 1011
768 150 160
97 728 10
6 7 2
406 409 10
571 8 3
40 77 75
767 769 1132
436 452 94
167 483 474
12 10 630
956 10 1003
131 87 165
533 95 271
1153 607 608
9 78 310
740 44 48
78 74 77
876 929 65
478 785 525
"""


def process_data(data):
    data = data.strip().split("\n")
    numbers_list = []
    for row in data[1:]:
        numbers = row.split(" ")
        num1, num2, num3 = [int(number) for number in numbers]
        numbers_list.append((num1, num2, num3))
      
    return numbers_list


def get_median(data):
    median_list = []
    for num1, num2, num3 in process_data(data):
        numbers = [num1, num2, num3]
        numbers.sort()
        median = numbers[1]
        median_list.append(median)

    return median_list


if __name__ == '__main__':
    medians = get_median(DATA)
    for num in medians:
        print(num, end=" ")
