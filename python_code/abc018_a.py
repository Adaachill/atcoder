s = [int(input()) for i in range(3)]
#print(max(max(s[1],s[2]),s[0]))
s_ =sorted(s, reverse=True) 
for i in range(len(s)):
    for j in range(len(s_)):
        if s[i] == s_[j]:
            print(j+1)

