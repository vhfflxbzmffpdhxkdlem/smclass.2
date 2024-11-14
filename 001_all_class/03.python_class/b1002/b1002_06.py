students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
]

ss = [3,'강감찬',100,90,99]

#students 에 ss를 추가하시오
students.append(ss)
print(students)

# 값이 2개 이상 저장하려면, 주소값
# 이순신인 데이터를 삭제하시오.
for idx,s in enumerate(students):
  if s[1] =='이순신':
    #students.remove(s) # remove
    del students[idx] # del
  
print(students)



# print(students) #한번에 모두 출력

# for s in students: # 1개씩 가져와서 출력
#   if s[1] == '유관순':
#     print(s)

#   # 이름이 유관순인것을 출력하시오.
