x=int(input())
h=int(input())
m=int(input())
print((x//60+h) + (x%60+m)//60)
print((x%60+m)%60)
