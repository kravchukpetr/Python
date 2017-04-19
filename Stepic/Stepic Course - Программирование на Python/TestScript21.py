s = [int(i) for i in input().split()]

for i in range(len(s)):
    if len(s) == 1:
        print(s[0], end=' ')
    elif i == 0:
        print((s[1] + s[-1]), end=' ')
    elif i == len(s)-1:
        print((s[0] + s[-2]), end=' ')
    else:
        print((s[i+1]+s[i-1]), end=' ')
