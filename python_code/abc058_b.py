# 文字列の結合。互い違い
# for をlen(O)で回る
o = input()
e = input()
for i in range(min(len(o),len(e))):
  print(o[i]+e[i],end="")
if len(o) > len(e):
  print(o[-1])
elif len(o) < len(e):
  print(e[-1])
else:
  pass
