def reverse(x: int) -> int:
    maxsize = 9223372036854775807
    rev = 0
    negative = -1 if x < 0 else 1
    while x != 0:
        pop = abs(x) % 10
        x = int(abs(x)/10)
        print(f"Pop {pop}, X {x}")
        if rev > maxsize or rev == maxsize / 10 and pop > 7:
            return 0
        rev = rev * 10 + pop
        print(rev)
    return negative * rev
assert reverse(123) == 321
assert reverse(-123) == -321
