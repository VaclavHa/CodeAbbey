data = """
14
498485758 -91399
-495353832 -55042
-475043625 -187950
-308232630 64980
0 49449
253525746 4255
-1020656241 -333058
614737028 39992
0 -48148
-838932515 -34055
-1306677420 -144504
-1218422820 67512
-1771718543 278594
-1197322384 -6255
"""

lines = data.strip().split('\n')

pairs = []
for line in lines:
    parts = line.split(" ")
    if len(parts) == 2:
        pairs.append((int(parts[0]), int(parts[1])))

results = []
for pair in pairs:
    division = pair[0] / pair[1]
    fract_part = abs(division - int(division))

    if fract_part == 0.5:
        if division > 0:
            division = int(division) + 1
        else:
            division = int(division) - 1
        results.append(division)
    else:
        results.append(round(division))

for res in results:
    print(f"{res} ")
