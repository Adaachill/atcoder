def print_ans(l,r,N):
  """print(sum(r)-sum(l)+N)
  Parameters
  --------------
  >>> print_ans([24],[30],1)
  7
  >>> print_ans([6,3],[8,3],2) 
  4
  """
  print(sum(r)-sum(l)+N)


  

def main():
  N = int(input())
  l = []
  r = []
  for i in range(N):
    s = list(map(int,input().split()))
    l.append(s[0])
    r.append(s[1])

  print_ans(l,r,N)


if __name__ == '__main__':
  main()

