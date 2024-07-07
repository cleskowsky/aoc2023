import re


def parse(s):
    return s.split()


# Part 1

def calibration_value(x):
    ints = re.findall('\d', x)
    return int(ints[0] + ints[-1])


# Sample input
inputs = parse(s='''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet''')
assert calibration_value(inputs[0]) == 12
assert sum(calibration_value(x) for x in inputs) == 142

# Answer
inputs = parse(open('day1.txt').read())
assert sum(calibration_value(x) for x in inputs) == 55017

# Part 2

assert len('three') == 5

words_to_numbers = {
    'zero': 0,
    '0': 0,
    'one': 1,
    '1': 1,
    'two': 2,
    '2': 2,
    'three': 3,
    '3': 3,
    'four': 4,
    '4': 4,
    'five': 5,
    '5': 5,
    'six': 6,
    '6': 6,
    'seven': 7,
    '7': 7,
    'eight': 8,
    '8': 8,
    'nine': 9,
    '9': 9
}


def calibrate_value2(s):
    x = []
    for i in range(len(s)):
        for num in words_to_numbers.keys():
            if s.find(num, i) == i:
                x.append(words_to_numbers[num])
    return 10 * x[0] + x[-1]


# Sample input
inputs = parse('''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen''')
assert calibrate_value2(inputs[0]) == 29
assert sum(calibrate_value2(s) for s in inputs) == 281

# Answer
inputs = parse(open('day1.txt').read())
sum(calibrate_value2(s) for s in inputs) == 53539
