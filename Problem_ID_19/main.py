def parse_data(input_data):
    parsed_data = []
    with open(input_data, mode="r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            parsed_data.append(line)
    return parsed_data


def check_brackets(data):
    left_brackets = "({[<"
    right_brackets = ")}]>"
    brackets_map = {")": "(", "}": "{", "]": "[", ">": "<"}
    results = []

    for line in data:
        stack = []
        valid = True
        for char in line:
            if char in left_brackets:
                stack.append(char)
            elif char in right_brackets:
                if stack and stack[-1] == brackets_map[char]:
                    stack.pop()
                else:
                    valid = False
                    break
        if stack:
            valid = False
        results.append("1" if valid else "0")

    return results


if __name__ == '__main__':
    INPUT = "input.txt"

    data_to_process = parse_data(INPUT)
    checked = check_brackets(data_to_process)

    for result in checked:
        print(result)
