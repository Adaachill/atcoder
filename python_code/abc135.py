#a,b = map(int,input().sprit())
n = int(input())
p = list(map(int,input().split()))
q = sorted(p)
j = 0 # index
count = 0 # swap count
ans = 0
for i in range(len(p)):
    if p[i] != q[i]:
        if count:
            ans = 1
            break
        elif j:
            if p[i] == q[j]:
                count += 1
            else:
                ans = 1
                break
        else:
            j = i
if ans == 1:
    print("NO")
else:
    print("YES")


