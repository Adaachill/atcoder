n = int(input())
s = [input() for _ in range(n)]
ans = 0
exclude = [] # 既に以前に同じアナグラムのものが存在するのでアナグラムを数える必要がない文字列の集合。数字で保存
for i in range(n-1):
  l = list(set(s[i]))
  if i in exclude:
    break # 既にそのアナグラムの文字列がいくつあるかは調べているので不要
  i_count = 1 # i番目の文字列と同じアナグラムが何個存在するか
  for j in range(n):
    if i < j:
      for k in range(len(l)):
        if s[i].count(l[k]) != s[j].count(l[k]):
          break
        if k == len(l)-1:
          exclude.append(j)
          i_count += 1 
  ans += i_count*(i_count-1)//2 # nC2
print(ans)
