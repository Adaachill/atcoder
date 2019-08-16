n = int(input())
max_1 = 0
max_2 = 0
a = []
id_1 = 0
for i in range(n):
  a.append(int(input()))
  if a[i] > max_1:
    id_1 = i
    max_1 = a[i]
  elif a[i] > max_2:
    max_2 = a[i]
for i in range(n):
  if id_1 == i:
    print(max_2)
  else:
    print(max_1)
