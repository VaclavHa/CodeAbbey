from math import sqrt

INPUT_DATA = "input.txt"


# Magical formula c = sqrt(a**2 + b**2)

def parse_data(input_data: str):
    """
    Parse data for triangle sides a, b, c
    :param input_data: String of numbers
    :return: list of sides a, b, c
    """
    sides = list()
    with open(INPUT_DATA, mode='r') as file:
        for line in file.readlines():
            a, b, c = line.strip().split()
            sides.append(tuple(map(int, [a, b, c])))
    return sides


def pythagorean(data: list):
    """
    Magical formula to declare if the triangle is Right, Acute or Obtuse
    :param data: list of sides a, b, c
    :return: list of strings "R", "A", "O"
    """
    results = list()
    for a, b, c in data:
        a, b, c = sorted([a, b, c])
        hypotenuse = sqrt(a ** 2 + b ** 2)
        if hypotenuse > c:
            print("A")
            results.append("A")
        elif hypotenuse < c:
            print("O")
            results.append("O")
        else:
            print("R")
            results.append("R")
    return results


if __name__ == '__main__':
    data = parse_data(INPUT_DATA)
    result = pythagorean(data)
    print(" ".join(result))
