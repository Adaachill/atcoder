# 先頭のB1から順番に処理をする
# Biはi番目に残っている敵の数をCiとして
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
sum = 0
c = a
for i in range(n):
    if c[i] > b[i]:
        sum += b[i] # 同じ街の敵のみ倒して終了
    elif c[i+1] > b[i] - c[i]: #次の街の敵も倒せるが、途中で力つきる
        sum += b[i]
        c[i+1] = c[i+1]-b[i]+c[i]
    else: #次の街まで全員倒した
        sum += c[i+1] + c[i]
        c[i+1] = 0
print(sum)
