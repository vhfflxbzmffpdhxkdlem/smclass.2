# [4,5] 2차원 리스트

# [0,3,6,9,...,57]
# aArr = []
# for i in range(20):
#   aArr.append(i*3)
# print(aArr)

# a_list = []
# for i in range(4):
#   a = []
#   for j in range(5):
#     a.append(aArr[5*i+j])
#   a_list.append(a)
# print(a_list)


# a_list = []
# for i in range(0,60,3):
#   a_list.append(i)
# print(a_list)
# b_list = []
# for i in range(4):
#   b = []
#   for j in range(5):
#     b.append(a_list[5*i+j])
#   b_list.append(b)
# print(b_list)


a_list = []
# for i in range(4):
#   a = []
#   for j in range(5):
#     #a.append(5*i(j+1))
#     a.append(5*3*i+(3*j))
#   a_list.append(a)
# print(a_list)


for i in range(4):
  for j in range(5):
    print(a_list[i][j],end="\t")
  print()