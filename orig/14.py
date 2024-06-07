for x in range(2031):
    a = 3**100 - x
    s = ''
    while a > 0:
        s = str(a % 3) + s
        a = a // 3
    if s.count('0') == 2:
        print(x) # = 1723