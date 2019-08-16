import string
def print_ans(s):

  A=string.ascii_lowercase
  B=list(set(A)-set(S))
  B.sort()
  print_ans(B[0] if B else 'None')

def main():
  S = input()
  print_ans(S)


if __name__ == '__main__':
    main()

