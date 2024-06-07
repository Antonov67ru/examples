def d(x):
    delit = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            delit.add(i)
            delit.add(x//i)
    return sorted(delit)

for x in range(600_001, 600_800 + 1):
    delit = [i for i in d(x) if i % 10 == 7 and i != 7]
    if len(delit) > 0:
        print(x, min(delit))