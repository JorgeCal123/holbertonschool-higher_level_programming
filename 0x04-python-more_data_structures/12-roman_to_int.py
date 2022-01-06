#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = []
    for i in roman_string:
        number.append(roman.get(i))
    j = 0
    total = number[0]

    while j < len(number) - 1:

        if(number[j] < number[j + 1]):
            total = number[j + 1] - total
        elif(number[j] >= number[j + 1]):
            total = number[j + 1] + total
        j += 1

    return total
