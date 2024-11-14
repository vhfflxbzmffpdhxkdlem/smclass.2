# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

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
    print("[ 학생성적입력 ]")
    while True:
      no = stuNo+1
      name = input(f"{no}번째 학생의 이름을 입력하세요.(0.이전페이지 이동)")
      if name =='0':
        break
      kor = int(input("국어성적을 입력해주세요."))
      eng = int(input("영어성적을 입력해주세요."))
      math = int(input("수학성적을 입력해주세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      s = {"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank}
      stuNo += 1
      students.append(s)

  elif choice == '2':
    print("[ 학생성적출력 ]")
    for s_t in s_title:
      print(s_t,end = "\t")
    print()
    print("-"*50)
    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")

  elif choice == '3':
    print("[ 학생성적수정 ]")
    name = input("성적을 수정할 학생이름을 검색해 주세요.")
    for s in students:
      if s['name'] == name:
        print("1. 국어")
        print("2. 영어")
        print("3. 수학")
        choice = input("수정할 성적의 과목을 선택해 주세요")
        if choice == '1':
          print(f"이전 국어성적{s['kor']}")
          s['kor'] = int(input("바뀔 국어성적"))
        elif choice == '2':
          print(f"이전 국어성적{s['eng']}")
          s['eng'] = int(input("바뀔 영어성적"))
        elif choice == '3':
          print(f"이전 국어성적{s['math']}")
          s['math'] = int(input("바뀔 수학성적"))
        s['total'] = s['kor']+s['eng']+s['math']
        s['avg'] = s['total']/3
    for s_t in s_title:
      print(s_t,end = "\t")
    print()
    print("-"*50)
    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  elif choice == '4':
    name = input("찾고자 하는 학생의 이름을 검색해 주세요.")
    for s in students:
      if s['name'].find(name) != -1:
        print(f"{name}학생을 찾았습니다.")
        for s_t in s_title:
          print(s_t,end = "\t")
        print()
        print("-"*50)
        for s in students:
          print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  elif choice == '5':
    print("[ 학생성적삭제 ]")
    name = input("성적을 삭제할 학생이름을 검색해주세요")
    for s in students:
      if s['name'] == name:
        print("정말 삭제하시겠습니까? 되돌릴수 없습니다.")
        print("1. 삭제  2. 취소")
        choice("원하시는 번호를 선택해 주세요.")
        if choice == '1':
          del(s)
          print(f"{name}학생의 성적을 삭제했습니다.")
        if choice == '2':
          print("이전페이지로 돌아갑니다.")
  elif choice == '6':
    for s in students:
      count = 1
      for s1 in students:
        if s['total'] < s1['total']:
          count += 1
          s['rank'] = count
    for s_t in s_title:
      print(s_t,end = "\t")
    print()
    print("-"*50)
    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  elif choice == '0':
    break