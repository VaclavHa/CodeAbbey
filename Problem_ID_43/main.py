DATA = """
0.86889364011586
0.53885426139459
0.26153196021914
0.59655858203769
0.31450493494049
0.62557103531435
0.70963861839846
0.23650257848203
0.46965171582997
0.2308253981173
0.60244012670591
0.21675606258214
0.67345558619127
0.45689735235646
0.68138099834323
0.78506631683558
0.55746126268059
0.92492659669369
0.036535108461976
0.49704467272386
0.54770870832726
0.28439092962071
0.94947695732117
0.94184708967805
0.11041330592707
0.50423385249451
0.77025222359225
"""


def process_data(data):
    data = data.strip().split("\n")
    numbers = [float(num) for num in data]

    return numbers


def dice_roll(numbers):
    result = []
    for num in numbers:
        roll = int(num * 6) + 1
        result.append(roll)

    return result


if __name__ == "__main__":
    numbers = process_data(DATA)
    result = dice_roll(numbers)

    for num in result:
        print(num, end=" ")