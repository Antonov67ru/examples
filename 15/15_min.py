def F(a, b, x):
    if a <= x <= b:
        return True
    else:
        return False

mn=10**9

for a in range(0, 100):
    for b in range(a, 100):
        k=0
        for i in range(1, 200):
            x = i/2
            if not( (F(10, 15, x) or F(20, 27, x)) ) or F(a, b, x):
                k=k+1

        if k==199:
            mn=min(mn, b-a)
print(mn)