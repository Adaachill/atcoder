n = int(input())
s = [input() for _ in range(n)]
ans = 0
for i in range(n-1):
  l = list(set(s[i]))
  for j in range(n):
    if i < j:
      for k in range(len(l)):
        if s[i].count(l[k]) != s[j].count(l[k]):
          break
        if k == len(l)-1:
          ans += 1
print(ans)
