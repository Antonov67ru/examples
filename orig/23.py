def f(a, b):
    if a < b: return 0
    if a == b: return 1
    if a > b: return f(a - 2, b) + f(a // 2, b)

print(f(30, 14) * f(14, 1))