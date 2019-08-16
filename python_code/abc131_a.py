def print_ans(s):
  """
  Parameters
  --------------
  >>> print_ans("2276")
  Bad
  >>> print_ans("3776") 
  Bad
  >>> print_ans("8080")
  Good
  """
  if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
    print("Bad")
  else:
    print("Good")
  

def main():
  s = input()
  print_ans(s)


if __name__ == '__main__':
  main()

