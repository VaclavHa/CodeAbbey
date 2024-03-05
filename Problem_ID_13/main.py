DATA = """
407281 54853284 14458177 703249 15 326446 221416669 258351 7 422162 184954 491564 425 905 255174044 47109779 69609740 3502 45386362 5197769 253 1461535 30927 46 4 11 31754460 190605 337557 179
"""


def process_nums(data):
    # Split the string into a list of numbers as strings
    str_nums = data.strip().split(" ")

    # Convert each number string to an integer, then to a string, and split into digits
    result = [[int(digit) for digit in str(num)] for num in str_nums]

    return result


def wsd(numbers):
    results_nums = []
    for each_list in numbers:
        summa = 0
        for index, digit in enumerate(each_list, start=1):
            summa += index * digit
        results_nums.append(summa)

    return results_nums


if __name__ == "__main__":
    nums = process_nums(DATA)
    results = wsd(nums)

    for num in results:
        print(num, end=" ")
