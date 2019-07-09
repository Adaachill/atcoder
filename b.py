#!/bin/env python3
def judge_dist(i,j,P,D):
    dist = 0
    for k in range(D):
        dist += (P[i][k] - P[j][k])**2
    square = dist**(1/2)
    if square - int(square) == 0:
        return 1
    else:
        return 0 

def main():
    n,D=map(int,input().split())
    P=[list(map(int,input().split())) for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                res += judge_dist(i,j,P,D)  
    print(res)

main()
