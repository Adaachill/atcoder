A,B,C,D = map(int,input().split())
if A > D or B < C:
  print(0)
elif A <= C and D <= B:
  print(D-C)
elif C <= A and B <= D:
  print(B-A)
elif A <= C and C <= B:
  print(B-C)
else:
  print(D-A)
  
  