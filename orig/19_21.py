def f(s, m):
    if s >= 69: return m % 2 == 0
    if m == 0: return 0
    g = [f(s + 1, m - 1), f(s * 2, m - 1)]
    return any(g) if (m - 1) % 2 == 0 else all(g)

print( [s for s in range(1, 69) if f(s, 2)]) # 19 = 34
print( [s for s in range(1, 69) if not f(s, 1) and f(s, 3)]) # 20 = 17 33
print( [s for s in range(1, 69) if not f(s, 2) and f(s, 4)]) # 21 = 32