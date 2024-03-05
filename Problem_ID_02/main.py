sequence = "715 258 699 814 311 345 1144 1056 535 1160 807 966 619 284 716 277 777 519 161 788 471 522 1261 510 503 1015 1192 1105 869 230 110 303 193 1007 345 180 618 730 130 666 244 1071 714 1163 384 808 580 1259 384 197"

new_sequence = sequence.split()
sequence_list= []
for i in new_sequence:
    sequence_list.append(int(i))
    
count = 0

for i in sequence_list:
    count += i

print(count)
