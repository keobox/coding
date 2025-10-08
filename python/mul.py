"""Find multiples of n"""

MAX = 100

n = int(input("n: "))
if 0 < n <= MAX:
    mul = [x for x in range(n, MAX + 1) if x % n == 0]
    print(mul)
