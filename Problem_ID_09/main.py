DATA = """
28
123 413 231
1379 1179 629
276 225 162
257 202 132
133 110 180
2673 1179 811
996 897 1929
1400 2180 869
1809 2903 931
750 565 772
210 532 238
2455 1518 949
166 110 362
291 363 644
656 2306 959
1963 1154 715
941 1315 520
959 1844 1175
603 1334 404
935 2760 1416
880 2001 608
2898 1217 861
381 184 123
1552 659 755
1100 462 347
242 259 588
648 1406 854
2174 1876 954
"""


def get_numbers(data):
    numbers_list = []
    data = data.strip().split("\n")
    for row in data[1:]:
        numbers = row.split(" ")
        a, b, c = [(int(num)) for num in numbers]
        numbers_list.append((a, b, c))
    return numbers_list


def check_sides(data):
    for a, b, c in get_numbers(data):
        if (a + b) > c and (a + c) > b and (b + c) > a:
            print("1 ")
        else:
            print("0 ")


if __name__ == '__main__':
    check_sides(DATA)
