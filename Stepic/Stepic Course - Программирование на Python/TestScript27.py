n = int(input())
a, s = 1, n
matrix = []
for i in range(n): matrix.append([0] * (n))
while a <= (s ** 2):
  for i in range(s-n, n):
    matrix[s-n][i] = a
    a += 1
  for i in range(s-n+1, n):
    matrix[i][n-1] = a
    a += 1
  for i in range(n-2, s-n-1, -1):
    matrix[n - 1][i] = a
    a += 1
  for i in range(n-2, s-n, -1):
    matrix[i][s-n] = a
    a += 1
  n -= 1
for i in range(len(matrix)):
  for j in range(len(matrix)): print(matrix[i][j], end=" ")
  print()
