n=int(input())
s = n % 100
d = n % 10
z = n // 10 % 10
if z!=1 and d==1:
    print (n,"программист")
elif z!=1 and d>=2 and d<=4 :
    print (n,"программиста")
else:
    print (n,"программистов")
