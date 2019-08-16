w = input()
emerge = []
ans = 0 
#if Yes 0, No 1
for i in w:
  if i not in emerge:
    if w.count(i) % 2 == 0:
      pass
    else:
      ans = 1
if ans:
  print("No")
else:
  print("Yes") 
