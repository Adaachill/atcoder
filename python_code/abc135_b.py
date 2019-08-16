#a,b = map(int,input().sprit())
n = int(input())
p = list(map(int,input().split()))
q = sorted(p)
j = 0 # index
mismatch_c = 0 # mismatch count
ans = 0
for i in range(len(p)):
    if p[i] != q[i]:
        if mismatch_c == 0:
            j = i
            mismatch_c += 1
        elif mismatch_c == 1:
            if p[i] == q[j]:
                mismatch_c += 1
                ans = 1
            else:
                break
        else:
            ans = 0
            break
if ans == 0:
    print("NO")
else:
    print("YES")


