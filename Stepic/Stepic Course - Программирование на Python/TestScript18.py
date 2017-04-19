s = input() + str(1)
c = 1
r = ''

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
    else:
        r += s[i] + str(c)
        c = 1
print(r)
