# a<6 0,6<=a<=12 b/2 ,else b
a,b = map(int,input().split())
ans = b
if a < 6:
  ans = 0
elif a <13:
  ans = b//2
print(ans)