"Fibonacci series: print first n numbers"

def fib(n):
    "Iterative"
    if n == 0 or n == 1:
        print(n)
    else:
        a = 0
        b = 1
        for i in range(n):
            temp = a + b
            print(temp)
            a = b
            b = temp

def fib_r(n):
    "Recursive, but slow"
    if n == 0 or n == 1:
        return n
    else:
        return fib_r(n - 1) + fib_r(n - 2)

if __name__ == "__main__":
    n = 10
    fib(n)
    print()
    # very inefficient
    for i in range(n):
        print(fib_r(i))
