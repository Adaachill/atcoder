#!/bin/env python
#｜sum(L)-sum(L-L[i])｜ が最少となるiの時のsum(L-L[i])を求める
def main():
  n,l = map(int,input().split())
  ans = (2*l+n-1)*n//2
  if l > 0:
    ans -= l
  elif l+n-1 <0:
    ans -= (l+n-1)
  print(ans)
main()
