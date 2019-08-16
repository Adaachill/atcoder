s = input()
s_odd = s[0::2]
s_even = s[1::2]
ans = min(s_odd.count("0")+s_even.count("1"),s_odd.count("1")+s_even.count("0"))
print(ans)
