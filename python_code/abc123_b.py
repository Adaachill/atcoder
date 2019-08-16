time = []
time_per_10 = []
time_mod_10 = []
for i in range(5):
    time.append(int(input()))
    time_per_10.append(time[i]//10)
    time_mod_10.append((time[i]-1)%10)

print(sum(time_per_10)*10 + 10*4 + min(time_mod_10)+1)
