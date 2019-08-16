def print_ans(N,L):
  """
  Parameters
  --------------
  >>> print_ans(5,2)
  18
  >>> print_ans(3,-1) 
  0
  >>> print_ans(30,-50)
  -1044
  """
  ans = 0
  if L >= 0:
    ans = (L+N-1+L+1)*(N-1)//2
  elif L+N-1 <= 0:
    ans = (L+N-2+L)*(N-1)//2
  else:
    ans = (L+N-1+L)*(N-1)//2

  print(ans)
  

def main():
  N,L = map(int,input().split())
  print_ans(N,L)


if __name__ == '__main__':
  main()

