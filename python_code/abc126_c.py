n,k = map(int,input().split())

i = 0
ans = 0
while (k-1)//(2**i) != 0:
  ans += ((k-1)//(2**i)) /((2**i)*n*2)
  i += 1
print(1-ans) 
