DATA = """
44 532627 791 573111021 4873709 8017185 61589 97014508 42278790 64548 2 138775 365690 830107525 8 338745 508 5916361 25575229 32954596 965356653 95742 3318
"""


def process_data(data):
    numbers = [int(num) for num in data.split(" ")]

    return numbers


def arr_checksum(numbers):
    result = 0
    for num in numbers:
        result += num
        result = (result * 113) % 10000007

    return result


if __name__ == "__main__":
    numbers = process_data(DATA)
    result = arr_checksum(numbers)

    print(result)
