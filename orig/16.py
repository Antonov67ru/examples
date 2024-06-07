from functools import *

@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return 2 * n * f(n-1)

for n in range(1, 10000):
    f(n)

print((f(2024) - 4 * f(2023)) // f(2022))