# 単純にループで開始位置と終了位置を指定するとO(n^2)*O(n)（話の計算にかかるコスト）で計算時間が間に合わない
# 先頭から和を取る中で、Kを超えたなら、開始位置が同じならその後は必ずKwを超えるのでa：は全て自然数より）
# その時のsum[i~j]-a[i]+a[j+1]>k かを判定するということを繰り返す。もし条件を満たすならi+=1でまだkにとどかないならj+=1とする。
def main():
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  ans = 0
  sum_a = 0
  i = 0#start position
  j = 0# end positon
  while True:
    sum_a += a[j]
    if sum_a >= k:
      if sum_a - a[i] <  k:
        ans += n-j
        break
      while sum_a - a[i] >= k:
        sum_a -= a[i]
        ans += n-j
        i += 1
    j += 1
    if j == n:
      
      break
    
  print(ans)

main()
