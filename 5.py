def f(s):
    return sum(int(j) for j in s)

for n in range(1, 100):
    s = bin(n)[2::]
    s = str(s)
    s = s + str(f(s) % 2)
    s = s + str(f(s) % 2)
    t = int(s, 2)
    if t > 77:
        print(n)
        break