# まず、x+y-k)%2==0の時、クリアできる。
k = int(input())
x,y = map(int,input().split())
if (x+y-k)%2 != 0:
    print(-1)
else:
    ans = (abs(x)+abs(y))//k
    a = x%k
    b = max(y%k,y%k-k)
    ans += 2*(min(b-a,b+a))
    
    for i in range(abs(x)//k):
        print(0,k*(i+1))
    for i in range(abs(x)//k):
        print(0,k*(i+1))
    print(ans)
