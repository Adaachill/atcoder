x,y = map(str,input().split())
print("<" if ord(x) < ord(y) else ">" if ord(x) > ord(y) else "=")
