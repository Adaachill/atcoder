n,k = map(int,input().split())
if n == k:
  print(1)
  for i in range(k-1):
    print(0)
  exit()
mod = 1000000007
Fact=[1]
for i in range(1,n+1):
  Fact.append(Fact[i-1]*i%mod)
Finv = [0]*(n+1) #階乗の逆元：1/(N!) あらかじめ計算しておかないと爆発する。
for i in range(n-1,-1,-1):
  Finv[i]=Finv[i+1]*(i+1)%mod
def comb(n,r):
  if n<0 or r<0:
    return 0
  if n < r:
    return 0
  return Fact[n]*Finv[r]*Finv[n-r]%mod
  
for i in range(1,k+1):
  ans=comb(k-1,i-1)*comb(n-k-1,i-2)+comb(k-1,i-1)*comb(n-k-1,i-1)*2+comb(k-1,i-1)*comb(n-k-1,i)
  print(ans%mod)  
