# x_(i+1) = x_i * r - D を x_(2010)まで計算し、出力する
# 単純に上の式でループを回すだけ
r,d,x = map(int,input().split()) 
x_i = [x]*11 # x_(2000~2010)
for i in range(1,11,1):
  x_i[i] = x_i[i-1]*r - d
  print(x_i[i])