# print max k (sum(l[0:k-1]) < x) l[0]+l[1]+...l[k-1] < x 
def main():
  n,x = map(int,input().split())
  l = list(map(int,input().split()))
  sum_l = 0
  ans = 0
  for i in range(n):
    sum_l += l[i]
    if sum_l > x:
      ans = i+1
      break
    ans = n+1 # when 
  print(ans)

main()
