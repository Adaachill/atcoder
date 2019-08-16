s = input()
print("Yes" if s[:-1].count(s[0]) >= 3 or s[1:].count(s[1]) >= 3 else "No") 
