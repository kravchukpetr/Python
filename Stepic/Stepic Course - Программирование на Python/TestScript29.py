def modify_list(l):
  k=[i//2 for i in l if i%2==0]
  l.clear()
  l+=k
