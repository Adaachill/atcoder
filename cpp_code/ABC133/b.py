def dist_D(a,b,D):
  square = 0
  for i in range(D):
    square += (a[i]-b[i])**2
  #print(square)
  if isinstance(square**(1/2),int):
    return 1
  else:
    return 0

def main():
  N,D = map(int,input().split())
  a = [[0 for i in range(D)] for j in range(N)]
  for i in range(N):
    a[i] = list(map(int,input().split()))
  ans = 0
  for i in range(N):
    for j in range(N):
      if j <= i:
        pass
      ans += dist_D(a[i],a[j],D)
  print(ans)

if __name__ == '__main__':
  main()
  