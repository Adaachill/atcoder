n = int(input())
t = list(map(int,input().split()))
sum_t = sum(t)
m = int(input())
s = [ input() for _ in range(m)]
p = [0]*m
x = [0]*m
for i in range(m):
  p[i],x[i] = map(int,s[i].split())
  print(sum_t - t[p[i]-1] + x[i])
