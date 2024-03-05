input_data = "32 185 473 175 379 307 309 307 479 44 389 118 132 189 250 412 182 234 154 416 348 220 480 526 168 87 283 474 477 503 524 70 411"

data = input_data.split(" ")

for temp in data[1:]:
    c = (int(temp) - 32) * 5 / 9 # formula to convert Fahrenheit to Celsius
    print(round(c), " ")
