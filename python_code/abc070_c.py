#import math
N = int(input())
T = []
for i in range(N):
  T.append(int(input()))
# output LCM(T1,T2... Tn)=LCM(Tn,LCM(Tn-1,LCM(...)))
def gcd(a,b): #Recusion!!
  if min(a,b) == 0:
    return max(a,b)
  else:
    return gcd(min(a,b),max(a,b)%min(a,b))
    
"""
  mi = min(a,b)
  ma = max(a,b)
  ans = 1
  '''for i in range(2,mi+1):
    if (mi%i)+(ma%i) == 0:
      mi /= i
      ma /= i
      ans *= i
      i -= 1'''
  while True:
    #print(ma,mi)
    if (ma % mi) == 0:
      ans = mi
      break
    else:
      mi = ma%mi
      ma = mi
      
  return ans"""


def lcm(a,b):
  #g = math.gcd(a,b)
  g = gcd(a,b)
  #print(g)
  return int(a*b//g)
ans = T[0]
for i in range(1,len(T)):
  ans = lcm(ans,T[i])
print(ans)
