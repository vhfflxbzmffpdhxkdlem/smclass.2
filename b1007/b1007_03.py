# 2차원 리스트
# for문을 2번 작성해서 1,25까지 [5,5] 리스트 생성하시오.
a_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(i*5+(j+1))
  a_list.append(a)
print(a_list)




#  a_list = []   # a_list[0],a_list[1],...  
# for i in range(9):
#   a_list.append(i+1)
# print(a_list)

# b_list = []
# for i in range(9):
#   b = []
#   if(a_list[i]%4)==0: #1,2,3,  4,5,6,   ,7,8,9
#     b.append(a_list[i])

# print(b_list)


# [3,3] 리스트 [1,2,3],[4,5,6],[7,8,9]
# 1-9까지 for문을 사용해서 ,2차원리스트에 추가하시오.
# a_list = []
# for i in range(0,3):
#   a = []
#   for j in range(0,3):
#     a.append(i*3+(j+1))
#   a_list.append(a)
# print(a_list)


# 1-9까지 for문을 사용해서, 리스트 추가하시오
# b_list = []
# for i in range(1,10):
#   b_list.append(i)
# print(b_list)


# a_list = [
#   [1,2],
#   [5,6,7,8],
#   [9,10,12]
# ]

# # 2차원리스트 -> for문을 2번 사용
# for i in a_list:
#   for j in i:
#     print(j)