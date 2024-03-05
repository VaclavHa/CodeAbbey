DATA = """
15
116 70 152
223 6 76
206 160 152
337 188 187
265 280 57
89 270 115
270 267 150
261 77 174
260 206 62
38 22 114
374 177 186
37 229 180
266 119 75
382 234 76
110 130 122
"""
numbers = [[int(num) for num in line.split()] for line in DATA.strip().split("\n")[1:]]

sums = []
for a, b, c in numbers:
    number = a * b + c
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10  # Add the last digit to the sum
        number //= 10  # Remove the last digit and continue
    sums.append(digit_sum)

for sum_of_digits in sums:
    print(sum_of_digits, end=" ")
