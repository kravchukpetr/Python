inf=open("sjat.txt")
ouf=open("razjat.txt","w")
for s1 in inf:
    s1=s1.strip()
    s1=s1+' '
    #print(s1)
    s2=''
    i=0
    while i<len(s1)-1:
        b=str(s1[i])
        n=int(s1[i+1])
        m=str(s1[i+2])
        if m.isdigit()==False:
            print(b*n,end='')
            ouf.write(b*n)
            i+=2
        else:
            #m=int(m)
            nm=int(str(n)+str(m))
            print(b*nm,end='')
            ouf.write(b*nm)
            i+=3
    ouf.write('\n')
ouf.close()
inf.close()
