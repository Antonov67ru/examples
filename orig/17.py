a = [int(x) for x in open('17.txt')]
s = []
mn = min([x for x in a])
for i in range(len(a) - 1):
    if((a[i] % 18) + (a[i + 1] % 18)) == mn:
        s.append(a[i] + a[i + 1])
print(len(s), max(s))