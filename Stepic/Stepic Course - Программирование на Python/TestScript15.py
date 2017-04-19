a=int(input())
b=int(input())
c=int(input())
d=int(input())
for k in range(c,d+1):
    print('\t',k,end='')
for k in range(a,b+1):
    print('\n',k,end='')
    for i in range(c,d+1):
        print('\t',i*k,end='')
