# Preparing Boxes
# i の倍数に入ったボールの数がai になる。箱iへのボールの入れ方が存在するかを判定する。
#  方針：N/2<i<N のiの倍数になる箱はiだけなので、b[i] = a[i]
# N/3<i<=N/2のとき、iの倍数になる箱はi,2iのみでb[i] = a[i]-b[i*2] XOR
# N/4<i<=N/3のとき、iの倍数になる箱はi,2i,3iのみでb[i] = a[i]-b[i*2]-b[i]
# python でのbit 演算 AND:& OR:| XOR:^ NOT:~ shift:<< >>1


n = int(input())
m = 0
a = list(map(int,input().split()))
b = []
for i in range(n,0,-1):
  if n // i >= 2:
# i の倍数の箱のボールの数とa[i] でXORをとってあげる。
    if ((sum([a[j-1] for j in a if j%i == 0]))%2)%2:
      b.append(i)
  else:
    if a[i-1] == 1:
      b.append(i)
print(len(b))
#print(b)
if len(b) != 0:
  print(*b)
