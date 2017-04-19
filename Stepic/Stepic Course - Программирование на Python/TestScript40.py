s=[int(i) for i in input().split()]
cnt = 0
summa = 0
dis = 0
for i in list(s):
    summa+=int(i)
    cnt+=1
av = summa/cnt
print(av)
for i in list(s):
	dis += (i - av)**2
print((dis/(cnt-1))**0.5)
