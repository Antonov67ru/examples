a={0: "А", 1: "О", 2: "У"}
count = 0
for i in range(0, len(a)):
    for k in range(0, len(a)):
        for r in range(0, len(a)):
            for q in range(0, len(a)):
                for d in range(0, len(a)):
                    count += 1
                    if count == 210:
                        print(a[i], a[k], a[r], a[q], a[d])