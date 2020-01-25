def romanToInt(s):
    numbers = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
    specials = {"IV": 4,
                "IX": 9,
                "XL": 40,
                "XC": 90,
                "CD": 400,
                "CM": 900}
    tocheck = ["I", "X", "C"]

    sum = 0
    index = 0
    while index < len(s):
        # check for specials
        if s[index] in tocheck:
            if s[index:index+2] in specials:
                sum = sum + specials[s[index:index+2]]
                index = index + 2
                continue
        sum = sum + numbers[s[index]]
        index = index +1
    print(sum)
    return sum
assert romanToInt("III") == 3
assert romanToInt("IV") == 4
assert romanToInt("IX") == 9
assert romanToInt("LVIII") == 58
assert romanToInt("MCMXCIV") == 1994

