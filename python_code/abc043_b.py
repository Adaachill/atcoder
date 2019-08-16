s = input()
ans = "" 
for i in s:
  if i == "B":
    if len(ans) == 0:
      pass
    else:
      ans = ans[:-1]
  else:
    ans += i
print(ans)
