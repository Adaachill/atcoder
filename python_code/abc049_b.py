h,w = map(int,input().split())
c = []
for i in range(h):
  c.append(input())
for i in range(2*h):
  for j in range(w):
    print(c[(i)//2][j],end="")
    if j == w-1:
      print("\n",end="")
