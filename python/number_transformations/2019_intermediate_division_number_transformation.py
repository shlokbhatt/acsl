# Lambert High School
# Author: Shlok Bhatt
# Date: 12/30/2024
# Description:

import csv


def transform_number(num, p):
    num = str(num)
    result = []

    for digit in num[:-p]:
        digit = int(digit)
        if digit + int(num[-p]) > 9:
            digit = (digit + int(num[-p])) % 10
        else:
            digit += int(num[-p])
        result.append(digit)

    result.append(int(num[-p]))

    for digit in num[-p+1:]:
        digit = abs(int(digit) - int(num[-p]))
        result.append(digit)

    return "".join(map(str, result[:len(num)]))


with open("2019_intermediate_division_number_transformation_input_file.txt", "r") as file:
    csv_reader = csv.reader(file, delimiter=' ')
    count = 1
    for line in csv_reader:
        print(str(count) + ". " + str(transform_number(int(line[0]), int(line[1]))))
        count += 1
