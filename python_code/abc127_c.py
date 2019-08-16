# master ID cardの数を求める問題
# 単純に考えてNまいのIDcardに対して、それが全てを通過できるか考えると、
# 計算量はO(N*M)かかるので10^5*10^5で10^10となり、通らない
# 番目の ID カードのうちどれか 1 枚を持っていれば通過できます。
# とのことから、i 番目のゲートを通るIDカードは連続で並んでいるので、
# Mのゲートに対して、開始点(Li)と終了点(Ri)のmax,minをとれば良い
n,m = map(int,input().split())
max_l = 0
min_r = n
for i in range(m):
  l,r = map(int,input().split())
  if max_l <  l:
    max_l = l
  if min_r > r:
    min_r = r
ans = 0
if min_r - max_l +1 > 0:
  ans = min_r - max_l +1
print(ans)
  
