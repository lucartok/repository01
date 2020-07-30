"""
https://www.codewars.com/kata/51b62bf6a9c58071c600001b/python

Create a function taking a positive integer as its parameter and returning a string
containing the Roman Numeral representation of that integer.
Modern Roman numerals are written by expressing each digit separately starting with
the left most digit and skipping any digit with a value of zero.
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1000
"""
symbols = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
    10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
    100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
    1000: 'M', 2000: 'MM', 3000: 'MMM'
}

number = input('Введите целое число от 1 до 3999: ')
number = number[::-1]
result = ''

for i in range(len(number) - 1, -1, -1):
    digit = int(number[i])*(10 ** i)
    if digit:
        result += str(symbols[digit])

print(result)
