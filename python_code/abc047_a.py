a = list(map(int,input().split()))
print("Yes" if sum(a)/2 in a and sum(a) % 2 == 0 else "No")
