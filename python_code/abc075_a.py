a = list(map(int,input().split()))
ans = [a[i] for i in range(3) if a.count(a[i]) == 1]
print(ans[0])
