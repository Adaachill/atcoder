s1=input()
s2=input()
ans = 0
for i in range(len(s1)):
    if s1[i] == s2[len(s1)-1-i]: ans += 1
if ans == len(s1):
    print("YES")
else:
    print("NO")
