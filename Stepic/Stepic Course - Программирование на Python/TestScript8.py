a=int(input())
b=int(input())
c=int(input())

if a>b:
    maxVal = a
    minVal = b
else:
    maxVal = b
    minVal = a
if c >  maxVal:
    srVal = maxVal
    maxVal = c
elif c < minVal:
    srVal = minVal
    minVal = c
else:
    srVal = c    
print(maxVal)
print(minVal)
print(srVal)
