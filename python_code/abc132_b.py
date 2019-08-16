def main():
  n = int(input())
  p = list(map(int,input().split()))
  ans = 0 
  up = 1 # state of up or down if up, p[i] < p[i+1]
  for i in range(n-2):
    """if p[i+1] > p[i+2]:
      up = 0"""
    if (p[i]-p[i+1])*(p[i+1]-p[i+2]) > 0 :
      ans += 1
  print(ans)
main()
