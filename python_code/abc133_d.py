
#!/bin/env python3
"""
1つ飛ばしで各ダムのsumを
"""
def main():
  n = int(input())
  a = list(map(int,input().split()))
  res = [0] * n
  sum_a = sum(a) #total rain 
  sum_odd = 0
  sum_even = 0
  for i in range(n):
    if i%2 == 1:
      sum_odd += a[i]
    else:
      sum_even += a[i]
  for i in range(n):
    if i == 0:
      res[i] = sum_a - (sum_even - a[i])*2
    else:
      res[i] = a[i]*2-res[i-1]
  for i in range(n):
    print(res[(i+n-1)%n],end=" ")
  print()
main() 
