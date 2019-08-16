def main():
  n = int(input())
  d = list(map(int,input().split()))
  ans = 0 
  d.sort()# distructive sort of list d
  if d[n//2 -1] != d[n//2]:
    ans = d[n//2] -d[n//2 -1] 
  print(ans)
main()
