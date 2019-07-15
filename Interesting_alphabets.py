import string
alpha = string.ascii_uppercase
num = int(input())
i = 0
l = list(alpha[0: num])
while i < num:
    print("".join(l[num - i - 1: num]))
    i += 1