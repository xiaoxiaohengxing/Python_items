i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d*%d=%-2d " % (i, j, i * j), end='')
        j += 1
    print("\n")
    i += 1