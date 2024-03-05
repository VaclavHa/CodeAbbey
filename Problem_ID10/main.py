# equation y(x) = ax + b
# to solve a = (y1 - y2) / (x2 -x1)
# to sovle b = y1 - a * x1


STRING = """
11
-707 -51045 897 62839
128 12462 -70 -7140
-328 -30336 -248 -22816
-435 -24041 -467 -25737
-297 21933 -487 36183
-253 10793 90 -4299
-286 -11970 -755 -31668
801 22218 184 5559
-676 -43692 541 34196
390 -12400 483 -15283
-471 -22999 -461 -22519
"""


def string_to_values(string: str):
    lines = string.strip().splitlines()[1:]
    values = []
    for line in lines:
        x1, y1, x2, y2 = map(int, line.split())
        values.append([(x1, y1), (x2, y2)])
    return values


def get_a_and_b(list_of_values: list):
    a_and_b_values = []
    for value in list_of_values:
        x1 = value[0][0]
        y1 = value[0][1]
        x2 = value[1][0]
        y2 = value[1][1]

        a_value = (y2 - y1) / (x2 - x1)
        a_value = round(a_value)

        b_value = y1 - a_value * x1
        b_value = round(b_value)

        a_and_b_values.append((a_value, b_value))

    return a_and_b_values


if __name__ == '__main__':
    values_to_proceed = string_to_values(STRING)
    result = get_a_and_b(values_to_proceed)

    for a, b in result:
        print(f"({a} {b})",end=" ")
