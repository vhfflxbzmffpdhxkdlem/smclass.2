# for문을 출력
for k in range(1,10):
  print(f"[ {k} 단 ]",end="\t")
print()

for i in range(2,10):
  for j in range(1,10):
    print(f"{j} x {i} = {i*j}",end="\t")
  print()

# 000
# 001
# ...
# 999
# for문 3개 사용
# for i in range(0,10):
#   for j in range(0,10):
#     for k in range(0,10):
#       print(f"{i}{j}{k}") 
# for문 1개 사용
# for i in range(1000):
#   print(f"{i:03d}")

# # 구구단 입력한 단까지 출력하시오. 3->1,2,3단 출력 5 -> 1,2,3,4,5 단 출력
# a = int(input("숫자를 입력하세요."))
# for s in range(a,a+1):
#   print(f"[ {s} 단 ]")
#   for i in range(1,10):
#     print(f"{s}x{i}={s*i}")