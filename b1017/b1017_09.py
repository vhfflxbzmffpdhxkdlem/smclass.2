import os

# isfile : 파일인지확인, isdir : 디렉토리인지 확인, exists :파일이 존재하는지
f = open("b1017/students.txt","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line:break
  print(line.strip())
f.close()




# if os.path.isfile("b1017/students.txt"):
#   print("파일이 존재 합니다.")
# else:
#   print("파일이 존재하지 않습니다.")