num = int(input())
n = num
i = 0
while n >= 0:
    if i % 2 == 0:
        print("1" * n)
    else:
        print("0" * n)
    n -= 1
    i += 1