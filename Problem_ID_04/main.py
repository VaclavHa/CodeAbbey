n = 22
data = """7518923 -846838
8007966 199228
-3424352 -6340881
3509932 749367
-7479656 2652763
8180754 -9160804
315962 3853582
7035098 8878231
-3202888 -7939129
-4411554 -9562267
-7325453 -5389229
6264874 9696481
3333552 2462851
-7807850 -4121836
2973973 -6820069
-1609958 3949069
-8377295 -8665171
199693 -3683729
-8143168 3585401
-3697741 9630573
3944478 496122
-694975 463641""".split("\n")

pairs = []


def get_pairs():
    for line in data:
        numbers = line.split()
        if len(numbers) % 2 == 0:
            pair = ((int(numbers[0])), (int(numbers[1])))
            pairs.append(pair)


def get_min_num():
    min_numbers = []
    for n1, n2 in pairs:
        if n1 > n2:
            min_numbers.append(n2)
        else:
            min_numbers.append(n1)
    print(" ".join(map(str, min_numbers)))


if __name__ == "__main__":
    get_pairs()
    get_min_num()
