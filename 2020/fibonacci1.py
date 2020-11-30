import sys

sys.setrecursionlimit(100000)

memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if(n == 1) or (n == 2):
        return 1
    r = fibonacci(n - 2) + fibonacci(n - 1)

    memo[n] = r

    return r

print(fibonacci(10000))