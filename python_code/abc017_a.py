a = [0]*3
b = [0]*3
sum = 0
for i in range(3):
    a[i],b[i] = map(int,input().split())
    sum += a[i]*b[i]//10
print(sum)
