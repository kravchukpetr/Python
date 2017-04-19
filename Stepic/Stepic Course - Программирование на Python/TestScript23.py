S = 0
s = 0
while True:
    a = int(input())
    s += a
    S += a**2
    if s == 0:
        break
print(S)
