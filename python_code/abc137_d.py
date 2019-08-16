# 見た感じDPで解けそう。
# i日後に得られる最大の報酬を考えて、Mまで増やしていく
# 漸化式はdp[i+1] = dp[i]+max(pay[i+1]) 
# pay[i]はi日目以内に報酬がもらえ、受けれる仕事の中で報酬が最大なもの
n,m = map(int,input().split())
a = [0]*n
b = [0]*n
for i in range(n):
  a[i],b[i] = map(int,input().split())
dp = [0]*(m+1)
job = [] #既にやった仕事
for i in range(1,m+1):
  job_i =job.index(max([j for j in range(n) if j not in job ]))
  dp[i] = dp[i-1] + b[job_i]
  job.append(job_i)
print(job)
print(dp[m])
