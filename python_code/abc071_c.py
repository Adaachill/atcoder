def print_ans(s):
  """
  Parameters
  --------------
  >>> print_ans([3,1, 2, 4, 2, 1])
  2
  >>> print_ans([1,2,3,4]) 
  0
  >>> print_ans([3,3,3,3,4,4,4,5,5,5])
  20
  """
  b = list(set(s)) # make unique list (no duplication)
  b.sort() # want to take max 
  ans = 1
  t = 0 # if t == 2, break
  while True:
    #print(len(b))
    if s.count(b[-1]) >= 4:
      ans = b[-1]**2
      break
    elif s.count(b[-1]) >= 2:
      ans *= b[-1]
      t += 1
      if t == 2:
        break
    if len(b) == 1:
      ans = 0
      break
    b.pop(-1) # skip b[-1]
      
  print(ans)

def main():
  N = input()
  A = list(map(int,input().split()))
  print_ans(A)


if __name__ == '__main__':
  main()

