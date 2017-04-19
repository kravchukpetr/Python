a=[]
while True:
  c=input()
  if c=='end':
    break
  s=[int(i) for i in c.split()]
  a.append(s)
line=len(a)
column=len(a[0])
b=[[0 for i in range(column)]for j in range(line)]
for i in range(-line,0):
    for j in range(-column,0):
        b[i][j]=(a[i+1][j]+a[i+line-1][j]+a[i][j+1]+a[i][j+column-1])
for i in range(line):
    for j in range(column):
        print (b[i][j],end=' ')
    print ("")
