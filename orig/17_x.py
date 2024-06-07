a = [int(x) for x in open('17.txt')]
b = []
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 2 == 0 and (a[i] % 19 == 0 or a[j] % 19 == 0):
            b.append(a[i] + a[j])

print(len(b), max(b))