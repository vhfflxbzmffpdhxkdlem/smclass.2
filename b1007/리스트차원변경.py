a_list = []
for i in range(25):
  a_list.append(i+1)
print(a_list)

# 1차원리스트 -> 2차원 리스트 변경
# (0,25,5씩증가)
b_list = []
for i in range(0,len(a_list),5):
  b_list.append(a_list[i:i+5])
print(b_list)


# 1차원리스트 -> 2차췅리스트 변경
# b_list = []
# for i in range(5):
#   a = []
#   for j in  range(5):
#     a.append(5*i+(j+1))
#   b_list.append(a)
