n,k = map(int,input().split())
s = input()
l = [0]
for i in range(n-1):
    if int(s[i])+int(s[i+1]) == 1:
      l.append(i+1)
l.append(n)
max = 0
m = 2*k +1
if len(l) <= m:
    #print(l)
    max = len(s)
if s[0] == 1:
    for i in range(0,len(l)-m,2):
       if l[i+m] - l[i] > max:
            max = l[i+m] - l[i]
else:
    for i in range(1,len(l)-m,2):
       if l[i+m] - l[i] > max:
            max = l[i+m] - l[i]
        
print(max)
