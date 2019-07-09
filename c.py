#!/bin/env python3
"""
引く必要はなかった
2019は素数でないから、673でも良い
"""
def main():
    l,r = map(int,input().split())
    res = 2019
    if r-l >= 2019:
      res = 0
    else:
      for i in range(l%2019,r-2019*(l//2019)+1):
        for j in range(i+1,r-2019*(l//2019)+1):
          res = min(res,(i*j)%2019)

    print(res)

main()
