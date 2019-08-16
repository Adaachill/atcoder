def gcd(i,j):
  if i > j:
    tmp = i
    i = j
    j = tmp
  while i != 0:
    tmp = i
    i = j%i
    j = tmp
  return j
def lcm(i,j):
  return i*j//gcd(i,j)  
def main():
  a,b,c,d = map(int,input().split())
  ans = b-a+1
  ans -= (b//c - (a-1)//c) + (b//d - (a-1)//d) - (b//lcm(c,d) -(a-1)//lcm(c,d))
  print(ans)


main()
