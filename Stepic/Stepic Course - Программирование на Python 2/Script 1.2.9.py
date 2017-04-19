objects = [1, 2, 1, 2, 3]
d = []
ans=0
for i in objects:
    if id(i) not in d:
        d.append(id(i))
        ans +=1     
print(ans)
