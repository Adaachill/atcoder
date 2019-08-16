x,y = map(int,input().split())
gp_1 = [1,3,5,7,8,10,12]
gp_2 = [4,6,9,11]
print("Yes" if (x in gp_1 and y in gp_1) or (x in gp_2 and y in gp_2) else "No")
