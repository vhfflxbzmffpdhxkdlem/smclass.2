import random

# 25개 1차원 리스트

# 25개 중 1을 5개 나머지는 0으로 입력해서 출력하시오.
# print([0]*20+[1]*5)
a_list = [0]*20+[1]*5
random.shuffle(a_list)
print(a_list)

#[5,5] 2차원리스트에 a_list의 값을 입력한후 출력하시오.
b_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(a_list[i*5+(j)])
  b_list.append(a)
print(b_list)

while True:
  print("\t0\t1\t2\t3\t4")
  print("-"*50)
  for i in range(5):
    print(i,end="\t")
    for j in range(5):
      print(b_list[i][j],end="\t")
    print()
  input1 = input("좌표를 입력해주세요.[0,1]")
  input2 = input1.split(",")
  print(input2)
  print(f"{input1} 좌표의 값 : ",b_list[int(input2[0])][int(input2[1])])

# [5,5] a_list 저장
for i in range(5):
  a = []
  for j in range(5):
    a.append(a_list[i*5+j]) #0,1,2,3,...24 # a_list 5개를 리릇트에 추가
  b_list,append(a) # a리스트를 b_list리스트에 추가
print(b_list)

# [5,5] 출력
while True:
  print("\t0\t1\t2\t3\t4")
  for i in range(5):
    for j in range(5):
      print(b_list[i][j],end="\t")
    print()

    num = input("좌표를 입력하세요.(0,0) >> ")
    num2 = num.split(",")
    print(f"{num2}좌표 값 : ",b_list[int(num[0])][int(num[1])])


#0:20개, 1:5개 생성
# a_list = []
# for i in range(25):
#   if i<20:
#     a_list.append(0)
#   else:
#     a_list.append(1)