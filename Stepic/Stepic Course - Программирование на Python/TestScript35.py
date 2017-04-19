with open(r'dataset_3363_4.txt', 'r') as inf:
    with open(r'out4.txt', 'w') as outf:
        sr = []
        for b in inf:
            b = b.strip().split(';')
            sr += b[1:]
            outf.write(str(sum(int(b[i]) for i in range(1, len(b))) / 3))
            outf.write('\n')
        for i in range(len(b) - 1):
            outf.write(str(float(sum(int(sr[k]) for k in range(i, len(sr), (len(b) - 1))) / (len(sr) / (len(b) - 1)))))
            outf.write(' ') 
