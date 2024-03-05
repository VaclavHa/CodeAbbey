n = 13
data = """898117 86945
413744 123297
12797 590374
447283 407375
360565 391257
780227 853389
465674 143375
569906 278769
675776 959685
800061 637354
145563 483154
477694 120282
903120 26942"""

lines = data.split("\n")

pairs = []

def get_pairs():
    for line in lines:
        numbers = line.split()
        if len(numbers) % 2 == 0:
            pair = (int(numbers[0]), int(numbers[1]))
            pairs.append(pair)

def multiply_numbers():
    result = []
    for n1, n2 in pairs:
        product = n1 + n2
        result.append(product)
    print(" ".join(map(str, result)))
        
if __name__ == "__main__":
    get_pairs()
    multiply_numbers()
        
