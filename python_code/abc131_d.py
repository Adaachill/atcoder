def main():
  n = int(input())
  task_list = [list(map(int,input().split())) for _ in range(n)]
  task_list.sort(key = lambda x:x[1])
  curr_time = 0 
  ans = 0 # if 1, say No
  
  for k in task_list:
    curr_time += k[0]
    if curr_time > k[1]:
      ans = 1
      break

  if ans == 1:
    print("No")
  else:
    print("Yes")

main()
