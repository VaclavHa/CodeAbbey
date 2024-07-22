INPUT = 'input.txt'

with open(INPUT, mode='r') as file:
    nums = file.read()

numbers = nums.strip().split()
list_of_nums = [int(x) for x in numbers]

steps = []

for x in list_of_nums:
    count = 0
    while True:
        if x == 1:
            break
        if x % 2 == 0:
            x = x / 2
            count += 1
        else:
            x = 3 * x + 1
            count += 1
    steps.append(count)

for num in steps:
    print(num, end=" ")