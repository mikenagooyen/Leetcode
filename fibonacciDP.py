from typing import List
def fib(n: int):
    if n == 1 or n == 2:
        return 1
    result = fib(n - 1) + fib(n - 2)

    return result

def fib_memo(n: int, memo: List[int]):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = result
    return result

def fib_2(n):
    memo = [None] * (n + 1)
    return fib_memo(n, memo)        

def fib_bottomup(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1

    for i in range(3, n + 1):
        result = fib_bottomup(n - 1) + fib_bottomup(n - 2)
    return result

def fib_bottomupDP(n):
    fib = [None] * (n + 1)
    for k in range(1, n + 1):
        if k <= 2: f = 1
        else: f = fib[k - 1] + fib[k - 2]
        fib[k] = f
    return fib

print(fib_2(10))
print(fib_bottomupDP(10))