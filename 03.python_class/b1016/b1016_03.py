# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0}
#   [1,"홍길동",100,100,99,299,99.67,0],
#   [2,"유관순",80,80,99,259,86.33,0],
#   [3,"이순신",100,99,90,289,96.33,0]
# ]
stu_key = ["no","name","kor","eng","math","total","avg","rank"]
students = []

# 파일 읽기 - r
f = open('a.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:break
  s = line.strip().split(",")
  s[0] = int(s[0])
  s[2] = int(s[2])
  s[3] = int(s[3])
  s[4] = int(s[4])
  s[5] = int(s[5])
  s[6] = float(s[6])
  s[7] = int(s[7])


  # for i,v in enumerate(s):
  #   if i == 1: continue
  #   elif i == 6: s[6]['avg'] = float(s[6]['avg'])
  #   else: s = int(v)


  students.append(dict(zip(stu_key,s)))
  print(line.strip())
f.close()
print(students)