data = [i.lower() for i in input().split()]
udata = set(data)
for i in udata:
    print(i, data.count(i))
