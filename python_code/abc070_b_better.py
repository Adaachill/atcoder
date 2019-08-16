A,B,C,D = map(int,input().split())
# distance from max of less value(A,C) to min of larger value
start = max(A,C)
end = min(B,D)
print(max(0,end-start))