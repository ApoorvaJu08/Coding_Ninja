import string
alpha = string.ascii_uppercase
n = int(input())
i = 0
while i < n:
    s = "".join(alpha[i: i+1])
    x = (i+1) * s
    print(x)
    i += 1