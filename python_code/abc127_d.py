# M回の操作終了後に N枚のカードに書かれた整数の合計の最大値を求めてください。
# で操作はB_j 枚以下の任意のカードをC_jに置き換えるという処理ができる。
# つまり、元のカードの値Aをソートして、小さいものから順にC_jの大きいもので並び替えれば良い
import sys
input=sys.stdin.readline
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
b_c = [list(map(int,input().split())) for _ in range(m)]
b_c.sort(key = lambda x:x[1], reverse=True) # c でソートする
pos = 0
ans = sum(a)
for i in range(m): # 一応最後までb_c をループするようにして、c よりも元のカードが大きくなったらbreakする
  if a[pos + b_c[i][0] - 1] > b_c[i][1]:
    for j in range(b_c[i][0]): #　何番目までは入れ替えた方が特か判定
      if a[pos + j] > b_c[i][1] or pos + j >= n:
        break
      else:
        ans += b_c[i][1] - a[pos + j] # 置き換えによる増加量
    break
  else:
    for j in range(b_c[i][0]): #　
      ans += b_c[i][1] - a[pos + j]
    pos += b_c[i][0]
print(ans)
# 最初はエラー : b_c[i][0]をb_c[0]でやっていたから
# 次は値がおかしい。sortがb_cは逆順（大きいものから順に）にする必要がある
# そのためには, reverse=True を入れる
# しかし、これでも入力例2で異なる答え、入力例4でエラーが出る。
# posをたす位置がおかしかった
# ここで提出したが、まさかのRE 時間がかかりすぎ
# 一応O(N)で収まっているはずだが、定数倍の高速化が必要
# https://qiita.com/fantm21/items/6df776d99356ef6d14d4
# https://atcoder.jp/contests/abc127/submissions/5599326
# うーんわからん
