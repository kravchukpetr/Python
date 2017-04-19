s = []
n_max = 0
with open('dataset_3363_3.txt') as sss:
    for i in sss:
      s += i.lower().split()
s.sort()
for i in s:
    if s.count(i) > n_max:
        n_max = s.count(i)
        w_max = i
print(w_max, n_max)
