s = [ input() for i in [0]*3]
current = 0
while len(s[current]) >= 0 :
  if len(s[ord(s[current][0]) - 97]) == 0:
    print(s[current][0].upper())
    break
  else:
    tmp = s[current][0] # 末尾の値を保存
    s[current] = s[current][1:] # 末尾を消去する
    current = ord(tmp) - 97
    # 末尾の値にcurrentを更新する

