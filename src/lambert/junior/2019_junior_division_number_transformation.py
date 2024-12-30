# Lambert High School
# Author: Shlok Bhatt
# Date: 12/30/2024
# Description:
# This script reads a text file containing rows of numbers and parameters, processes the numbers
# based on the given parameters using the `transform_number` function, and prints the transformed results.
#
# The input text file should have space-separated values where:
# - The first number is the input to be transformed,
# - The second number (p) indicates the position from the right of the digit to transform,
# - The third number (d) is used to compute the transformation.
#
# Example Input File (2019_junior_division_number_transformation_input_file.txt):
# 123456 3 2
# 789012 4 5

import csv


def transform_number(num, p, d):
    num = str(num)
    # print(len(num) - p)

    pth_digit = int(num[-p])
    # print("pth_digit = " + str(pth_digit))

    if 0 <= pth_digit <= 4:
        diff = pth_digit + d
        unit_digit = diff % 10
        # print("unit_digit = " + str(unit_digit))

        num = num[:-p] + str(unit_digit) + len(num[-p+1:]) * '0'
    elif 5 <= pth_digit <= 9:
        diff = abs(pth_digit - d)
        leftmost_digit = str(diff)[0]
        if -p + 1 == 0:
            num = num[:-p] + leftmost_digit
        else:
            num = num[:-p] + leftmost_digit + len(num[-p + 1:]) * '0'

    return num


with open("2019_junior_division_number_transformation_input_file.txt", "r") as file:
    csv_reader = csv.reader(file, delimiter=' ')
    count = 1
    for line in csv_reader:
        print(str(count) + ". " + str(transform_number(int(line[0]), int(line[1]), int(line[2]))))
        count += 1
