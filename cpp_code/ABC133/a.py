def main(N,A,B):
  print(min(N*A,B))

if __name__ == '__main__':
  N,A,B = map(int,input().split())
  main(N,A,B)