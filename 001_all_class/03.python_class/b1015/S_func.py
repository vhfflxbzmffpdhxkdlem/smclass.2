# students 리스트 타입
# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
#   {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
#   {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
#   {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
#   {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
# ]
students = []
stu_keys = ["no","name","kor","eng","math","total","avg","rank"]

f = open('students.txt','r',encoding='utf-8')
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
  s[7] = int(s[0])
students.append(dict(zip(stu_keys,s)))
for i in range(7):
  if i == 1: continue
  elif i == 6: s[6] = float(s[6])
  else:s[i] = int(s[i])
students.append(dict(zip(stu_keys,s)))
print(line.strip())
f.close
#-----------------------

# 5명 - 1,4,5 -> 4+1

stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
choice = 0 # 전역변수
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# 메뉴출력함수 시작
def title_program():
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
  return choice
# --------------------
# 학생성적입력함수 시작 - 일반변수 변경
def stu_input():
  while True:
      print("[ 학생성적 입력 ]")
      # 학생성적 직접 입력
      no = stuNo + 1  # 리스트 - 학생수
      name = input(f"{no}번째 학생 이름을 입력하세요.(0.이전화면) >>")
      if name == "0":
        print("성적입력을 취소합니다.")
        print()
        break
      kor = int(input("국어점수를 입력하세요."))
      eng = int(input("영어점수를 입력하세요."))
      math = int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      ss = { "no":no,"name":name,"kor":kor,"eng":eng,
             "math":math,"total":total,"avg":avg,"rank":rank }
      students.append(ss)
      stuNo += 1  # 학생수 1증가

      # students.txt 파일쓰기
      f = open('students.txt','w',encoding='utf-8')
      data = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
      f.write(data)
      f.close()
      #-----------------------
      print(f"{name} 학생성적이 저장되었습니다.!")
      print()
  return stuNo
# --------------------
# 학생성적출력 함수 선언
def stu_output():
    print("[ 학생성적 출력 ]")
    print()
    # 상단출력
    for st in s_title:
      print(st,end="\t")
    print(); print("-"*60)
    # 학생성적출력
    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()
#------------------------------
# 학생성적수정 함수 시작
def stu_update():
  print("[ 학생성적수정 ]")
  name = input("찾고자하는 학생의 이름을 입력하세요")

  # 전체학생과 비교
  flag = 0
  for s in students:
    if name == s['name']:
      print(f"{name}학생을 찾았습니다.")
      print("[ 수정 과목 선택 ]")
      print("1. 국어점수")
      print("2. 영어점수")
      print("3. 수학점수")
      choice = input("원하는 번호를 입력해주세요.>>")
      if choice == '1':
        print("이전 국어점수 : {}".format(s['kor']))
        s['kor'] = int(input("변경 국어점수 : "))
      elif choice =='2':
        print("이전 영어점수 : {}".format(s['eng']))
        s['eng'] = int(input("변경 영어점수 : "))
      elif choice =='3':
        print("이전 수학점수 : {}".format(s['math']))
        s['math'] = int(input("변경 수학점수 : "))
      s['total'] = s['kor']+s['eng']+s['math']
      s['avg'] = s['total']/3
      print(f"{name}학생성적이 수정되었습니다.")

      # 수정된 학생성적 출력 - 학생성적출력함수 재사용
      stu_output([s])

      flag = 1
    # 학생이 검색되지 않았을때
  if flag == 0 :
    print(f"{name}학생이 없습니다. 다시 입력하세요")
# --------------------------
# 학생성적검색 함수시작
def stu_selsct():
  flag = 0
  name = input("검색하려는 이름을 입력하세요.")
  sArr = []
  for idx,s in enumerate(students):
    if s['name'].find(name) != -1:
      # print(f"{idx+1}번째,{name} 학생을 찾았습니다.",s["name"])
      sArr.append(s)
      flag = 1
  if flag == 0:
    print(f"{name}학생을 찾을수 없습니다. 다시 입력해주세요.")
  else:
    print(f"{name} 이름으로 {len(sArr)}명 검색되었습니다.")
    stu_output(sArr)
#-----------------------------------
# 학생성적 삭제함수 시작
def stu_delete():
  print("[ 학생성적 삭제 ]")
  name = input("찾고자 하는 학생의 이름을 입력하세요.")
  flag = 0
  sArr = []
  for idx,s in enumerate(students):
    if s['name'] == name:
      flag = 1
      print(f"{name} 학생성적을 삭제하시겠습니까?(삭제시 복구불가)")
      print("1.삭제 2.취소")
      choice = input("원하는 번호를 입력하세요.>>")
      if choice == '1':
        sArr.append(s)
        del students[idx]
        print(f"{name} 학생성적이 삭제되었습니다.")
      else:
        print("학생성적 삭제가 취소되었습니다.")
      break
  if flag == 0 :
    print(f"{name} 학생이 없습니다. 다시 입력하세요.")
  else:
    stu_output([s])
#---------------------------------
# 등수처리함수 시작
def stu_rank():
  print("[ 등수처리 ]")
  for s in students:
    count = 1
    for st in students:
      if s['total'] < st['total']:
        count += 1
    s['rank'] = count # 등수입력
  print("등수처리가 완료되었습니다.")
  print()
  stu_output()
#---------------------------------
# 학생성적정렬 함수시작
def stu_sort():
  while True:
    print("[ 학생성적 정렬 ]")
    print("1. 이름 순차정렬")
    print("2. 이름 역순정렬")
    print("3. 합계 순차정렬")
    print("4. 합계 역순정렬")
    print("5. 번호 순차정렬")
    print("0. 이전페이지 이동")
    print("-"*40)
    choice = input("원하는 번호를 입력하세요.>> ")
    if choice == "1":
      #리스트를 1개 가져와서 딕셔너리중 이름을 가져와서 리턴
      students.sort(key=lambda x:x['name']) 
    elif choice == "2":
      students.sort(key=lambda x:x['name'],reverse=True)
    elif choice == "3":
      students.sort(key=lambda x:x['total'])
    elif choice == "4":
      students.sort(key=lambda x:x['total'],reverse=True)
    elif choice == "5":
      students.sort(key=lambda x:x['no'])
    elif choice == "0":
      print("이전페이지로 이동합니다.")
      break
    print("정렬이 완료되었습니다.")

#---------------------------------