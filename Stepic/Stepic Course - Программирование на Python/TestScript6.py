a=float(input())
b=float(input())
oper=(input())
if oper=='+':
    print(a+b)
if oper=='-':
    print(a-b)
if oper=='*':
    print(a*b)
if oper=='pow':
    print(a**b)    
if (oper=='/' or oper=='mod' or oper=='div') and b==0:
    print('Деление на 0!')
elif oper=='/':
        print(a/b)
elif oper=='mod':
        print(a%b)
elif oper=='div':
        print (a//b)
