name = ""; kor = 0; eng = 0; math = 0; total = 0; avg = 0; chk = 0; no = 1 ; rank = 0;count = 1
students = []
s_title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
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
      s = [no,name,kor,eng,math,total,avg,rank]
      students.append(s)
      no += 1


  elif choice == '2':
    print("[ 학생성적출력 ]")
    for s_t in s_title:
      print(s_t,end="\t")
    print()
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")


  elif choice == '3':
    print("[ 학생성적수정 ]")
    name = input("찾고자하는 학생이름을 검색해주세요")
    for s in students:
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        print("1. 국어")
        print("2. 영어")
        print("3. 수학")
        choice = input("수정할 과목을 선택해주세요")
        if choice == '1':
            print("이전 국어성적 : ",s[2])
            s[2] = int(input("수정될 국어성적 : "))
        if choice == '2':
            print("이전 국어성적 : ",s[3])
            s[3] = int(input("수정될 국어성적 : "))
        if choice == '3':
            print("이전 국어성적 : ",s[3])
            s[3] = int(input("수정될 국어성적 : "))
        s[5]=s[2]+s[3]+s[4]
        s[6]=s[5]/3
      if s[1] != name:
        print(f"{name} 학생이 없습니다.")


  elif choice == '4':
    print("[ 학생성적검색 ]")
    name = input("찾고자하는 학생이름을 검색해주세요")
    for s in students:
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        for s_t in s_title:
         print(s_t,end="\t")
        print()
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
      if s[1] != name:
        print(f"{name} 학생이 없습니다.")

        
  elif choice == '5':
    print("[ 학생성적삭제 ]")
    name = input("성적기록을 삭제할 학생이름을 검색해주세요")
    for idx,s in enumerate(students):
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        print("1. 삭제")
        print("2. 취소")
        choice = input("정말 삭제하시겠습니까?")
        if choice =='1':
          print(f"{name} 학생의 성적을 삭제합니다.")
          del students[idx]
        if choice == '2':
          print("성적 삭제를 취소합니다.")


  elif choice == '6':
    print("[ 등수처리 ]")
    for s in students:
      count = 1
      for st in students:
        if s[5] < st[5]:
          count += 1
      s[7] = count 

  elif choice =='7':
    print("[ 학생성적정렬]")

  elif choice == '0':
    print("프로그램을 종료합니다.")
    break
