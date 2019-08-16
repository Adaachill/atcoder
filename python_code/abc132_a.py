#!/bin/env python
#長さが4の文字列で、２種の文字が２回ずつ現れる文字列かどうか判定

def main():
  s = input() # len(s) == 4
  if s[0] != s[1]:
    if s.count(s[0]) == 2 and s.count(s[1]) == 2:
      print("Yes")
    else:
      print("No")
  elif s.count(s[0]) == 2 and s.count(s[3]) == 2:
    print("Yes")
  else:
    print("No")

main()
