n,s,t = map(int,input().split())
w = int(input())
a = [int(input()) for i in range(n-1)]
a.insert(0,w)
ans = 0
for i in range(n):
    #if sum(n[:i+1]) >= s and sum(a[:i+1]) <= t:
        ans += 1
print(ans)
