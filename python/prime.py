"""Prime numbers"""

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
    return True

def get_primes(n):
    """Use sieve of Eratosthenes"""
    if n <= 1:
        return []
    nums = range(2, n)
    i = 0
    while i < len(nums):
        erasing = nums[i]
        nums = [x for x in nums if x == erasing or x % erasing]
        i += 1
    return nums

def big_primes(n):
    i = 0
    while i < n:
        is_prime(i)
        i += 1

def perf_test(n):
    from timeit import default_timer as timer
    print("big primes", n)
    start = timer()
    big_primes(n)
    end = timer()
    print(end - start)
    print("big sieve", n)
    start = timer()
    get_primes(n)
    end = timer()
    print(end - start)

if __name__ == "__main__":
    for i in range(48):
        if is_prime(i):
            print(i)
    print()
    for i in get_primes(48):
        print(i)
    print()
    perf_test(100_000)

