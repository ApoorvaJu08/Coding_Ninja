n = int(input())
for i in range(n):
    for j in range(0, i+1):
        if i % 2 == 0:
            print(i + 1, end = ' ')
        else:
            if j > 0:
                i = i - 1
                print(i+2, end = " ")
            else:
                print(i + 2, end = " ")
    print()