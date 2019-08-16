# 文字列の結合は+,+=か、a.join(b)を使う
# 文字列のリストのソート。数字のリストのソートと変わらない。list.sort()でOK
n,l = map(int,input().split())
s = [ input() for _ in range(n)]
s.sort()
ans = "" #empty string
for i in range(n):
  ans += s[i]
print(ans)
