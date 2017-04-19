a = sorted([int (i) for i in input().split()])
r=[] 
for i in range(len(a)):
    if a.count(a[i]) > 1:
        if a[i] not in r:
            r.append(a[i])
            print(a[i],end=" ")
