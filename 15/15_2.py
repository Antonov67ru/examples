k = 0
for A in range(1, 300):
    count = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if ((x < A) <= (x * x < 81)) and ((y * y <= 36) <= (y <= A)):
                count += 1
    if (count == 90_000):
        k += 1
print(k)