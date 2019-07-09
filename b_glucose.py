from math import floor,ceil
n,d=map(int,input().split())
P=[list(map(int,input().split())) for _ in range(n)]
def judge(A,B):
    d=len(A)
    s=0
    for i in range(d):
        s+=(A[i]-B[i])**2
    s=s**0.5
    return floor(s)==ceil(s)
ans=0
for i in range(n):
    for j in range(i+1,n):
        ans+=judge(P[i],P[j])
print(ans)
