w,h,n = map(int,input().split())
s = [ input() for _ in range(n)]
x = [0]*n
y = [0]*n
a = [0]*n
for i in range(n):
  x[i],y[i],a[i] = map(int,s[i].split())
x_1 = max(0,max([x[i] for i in range(n) if a[i] == 1])
x_2 = min(0,min([x[i] for i in range(n) if a[i] == 2])
y_1 = max([y[i] for i in range(n) if a[i] == 3])
y_2 = min([x[i] for i in range(n) if a[i] == 4])
print((x_2 - x_1) * (y_2 - y_1))
