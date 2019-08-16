# a-k = k-b (if a>b) k -a = b-k (if a < b)
# a+b = 2k 
# if a+b % 2 == 1 IMPOSSIBLE else a+b/2
a,b = map(int,input().split())
if (a+b) % 2:
    print("IMPOSSIBLE")
else:
    print((a+b)//2)
