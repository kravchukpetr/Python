n = int(input())
def show(n):
    i = 0
    for j in range(1,n + 1):
        for p in range(1,j +1):
            i = i + 1
            if(i <= n):
                print(j,end=' ');
            else:
                break;
        if (i > n):
            break;     
show(n) 
