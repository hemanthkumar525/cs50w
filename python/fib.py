def fib(n: int) -> int:
    curr, prev = 1, 0
    for i in range(n-1):
        curr, prev = curr + prev, curr
    return