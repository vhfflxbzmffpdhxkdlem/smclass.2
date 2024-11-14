# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
stuNo = len(students)+1  # 학생번호 생성
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

s_title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
# 학생성적프로그램
while True:
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

  if choice == '1':
      while True:
        print("[ 학생성적입력 ]")
        name = input("학생이름을 입력해주세요(상위폴더로 이동:0)")
        if name == '0':
          print("상위폴더로 이동합니다.")
          break
        kor = int(input("국어점수를 입력해주세요"))
        eng = int(input("영어점수를 입력해주세요"))
        math = int(input("수학점수를 입력해주세요"))
        total = kor+eng+math
        avg = total/3
        ss = {
          "no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank
        }
        students.append(ss)
        no += 1


  elif choice == '2':
    print("[ 학생성적출력 ]")
    for s_t in s_title:
      print(s_t,end="\t")
    print()
    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()


  elif choice == '3':
    print("[ 학생성적수정 ]")
    name = input("찾고자하는 학생의 이름을 입력해주세요")
    for s in students:
      if s["name"] == name:
        print("1. 국어성적")
        print("2. 영어성적")
        print("3. 수학성적")
        choice = input("수정할 과목을 선택해 주세요.")
        if choice == '1':
          print(f"이전 국어성적 : {s["kor"]}")
          s["kor"] = input("수정할 국어성적 : ")
        elif choice == '2':
          print(f"이전 영어성적 : {s["eng"]}")
          s["eng"] = input("수정할 영어성적 : ")
        elif choice == '3':
          print(f"이전 수학성적 : {s["math"]}")
          s["math"] = input("수정할 수학성적 : ")
        s["total"] = int(s["kor"])+int(s["eng"])+int(s["math"])
        s["avg"] = s["total"]/3
      elif s["name"] != name:
        print("찾고자하는 학생이 없습니다.")

  elif choice =='4':
    print("[ 학생성적검색 ]")
    name = input("찾고자하는 학생의 이름을 입력해주세요")
    for s in students:
      if s["name"] == name:
        for s_t in s_title:
          print(s_t,end="\t")
        print()
        for s in students:
          print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
      elif s["name"] != name:
        print("찾고자하는 학생이 없습니다.")
  elif choice == '5':
    print("[ 학생성적삭제 ]")

  elif choice == '7':
    while True:
      print("[ 학생성적 정렬 ]")
      print("1. 이름으로 순차정렬")
      print("2. 이름으로 역순정렬")
      print("3. 합계로 순차정렬")
      print("4. 합계로 역순정렬")
      print("5. 번호 순차정렬")
      print("0,  이전페이지 이동")
      print("-"*40)
      choice = input("원하는 번호를 입력하세요.>>")
      if choice == '1':
        students.sort(key=lambda x:x['name'])
      elif choice =='2':
        students.sort(key=lambda x:x['name'],reverse=True)
  elif choice == '0':
    print("프로그램을 종료합니다.")
    break
  print("정렬이 완료되었습니다.")









# no = 1; name  = "";kor = 0; eng = 0;math = 0;total = 0;avg = 0;rank = 0;
# count = 1
# t = ["번호","이름","국어","영어","수학","합계","평균","등수"]
# ss = [no,name,kor,eng,math,total,avg,rank]
# #
# # 학생성적 입력부분을 구현하시오.
# # dict타입으로 입력을 할것
# # 번호,이름,국어,영어,수학,합계,평균,등수
# # 입력이 완료되면 출력이 바로 되도록 하시오.
# while True:
#   name = input("이름을 입력해주세요")
#   kor = int(input("국어성적을 입력해주세요"))
#   eng = int(input("영어성적을 입력해주세요"))
#   math = int(input("수학성적을 입력해주세요"))
#   total = kor+eng+math
#   avg = total/3
#   ss = [no,name,kor,eng,math,total,avg,rank]




