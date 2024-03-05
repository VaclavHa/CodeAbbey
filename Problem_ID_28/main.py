DATA = """
33
76 2.33
78 1.45
85 1.56
94 1.80
119 1.99
47 1.53
120 1.91
114 1.76
92 1.78
47 1.62
108 1.78
42 1.15
114 3.08
112 2.37
55 1.25
86 2.68
82 2.34
103 1.74
57 2.09
99 2.66
96 2.14
89 2.72
104 2.47
115 2.53
89 2.22
89 2.01
96 1.96
47 1.77
81 2.18
118 2.72
58 1.44
96 1.85
116 2.04
"""


def parse_data(data: str) -> list:
    data = data.strip().split("\n")
    return [tuple(map(float, row.split())) for row in data[1:]]


def get_bmi(data):
    for weight, height in parse_data(data[1:]):
        BMI = weight / height ** 2
        if BMI < 18.5:
            print("under", end=" ")
        if 18.5 <= BMI < 25.0:
            print("normal", end=" ")
        if 25.0 <= BMI < 30.0:
            print("over", end=" ")
        if 30.0 <= BMI:
            print("obese", end=" ")


if __name__ == '__main__':
    get_bmi(DATA)
