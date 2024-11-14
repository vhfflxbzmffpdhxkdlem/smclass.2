subName = ["국어","영어","수학"]
score = {"국어":100,"영어":95,"수학":80}
print(score)
print(score['국어'])
print(subName[0])
print(score[subName[0]])

for i in range(3):
  print(f"{subName[i]} : {score[subName[i]]}")

for k,v in score.items():
  print(k,":",v)
for i in subName:
  print(i,":",score[i])

# def gugu(n2):
#   for i in range(2,n2+1):
#     print(f"[ {i} 단 ]")
#     for j in range(1,10):
#       print(f"{i} * {j} = {i*j}")

# nArr = [9,5,7]

# # 2-9, 2-5, 2-7
# # gugu(9)
# # gugu(5)
# # gugu(7)

# for i in nArr:
#   gugu(i)
#   print("-"*50)


# # 구구단을 출력하시오.
# def gugu(n1,n2):
#   for i in range(n1,n2):
#     print(f"[ {i} 단 ]")
#     for j in range(1,10):
#       print(f"{i} * {j} = {i*j}")
 
# # 2-5
# # for i in range(2,6):
# #   print(f"[ {i} 단 ]")
# #   for j in range(1,10):
# #     print(f"{i} * {j} = {i*j}")
# gugu(2,6)
# # 3-9
# # for i in range(2,10):
# #   print(f"[ {i} 단 ]")
# #   for j in range(1,10):
# #     print(f"{i} * {j} = {i*j}")
# gugu(3,10)
# # 5-8
# # for i in range(5,9):
# #   print(f"[ {i} 단 ]")
# #   for j in range(1,10):
# #     print(f"{i} * {j} = {i*j}")
# gugu(5,9)