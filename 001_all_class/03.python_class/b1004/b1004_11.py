students = []
no = 1
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
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
  print("0. 프로그램을 종료")
  print("-"*60)

  choice = input("원하는 번호를 입력하세요.(종료:0)>>")

  if choice =='1':
    print("[ 학생성적입력 ]")
    name = input("이름을 입력해주세요")
    if name =='0':
      print("상위폴더로 이동합니다.")
      break
    kor = int(input("국어점수를 입력해 주세요"))
    eng = int(input("영어점수를 입력해 주세요"))
    math = int(input("수학점수를 입력해 주세요"))
    total = kor+eng+math
    avg = total/3
    rank = 0
    s = [no,name,kor,eng,math,total,avg,rank]
    students.append(s)
    print(f"번호:{no} 이름:{name} 국어:{kor} 영어:{eng} 수학:{math} 합계:{total} 평균:{avg:.2f} 등수:{rank}")


  if choice =='2':
    print("[ 학생성적확인 ]")
    for st in s_title:
      print(st,end='\t')
    print()
    print("-"*60)
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")


  if choice =='3':
    print("[ 학생성적수정 ]")
    search = input("찾는 학생 이름을 검색해주세요")
    for s in students:
      if s[1] == search:
        print("찾는 학생이 있습니다.")
        print(s)

        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        print("0. 상위폴더로 이동")
        choice = input("원하시는 번호를 입력해주세요.(상위폴더로 이동:0)")

        if choice == 1:
          for s in students:
            print("현재 국어점수는",s[2])
            kor_input = (input("수정할 점수를 입력해주세요"))
            s[2] = kor_input
        elif choice == 2:
          for s in students:
            print("현재 영어점수는",s[3])
            kor_input = (input("수정할 점수를 입력해주세요"))
            s[3] = kor_input
        elif choice == 3:
          for s in students:
            print("현재 영어점수는",s[4])
            kor_input = (input("수정할 점수를 입력해주세요"))
            s[4] = kor_input
        elif choice == 0:
          print("상위폴더로 이동합니다.")
          break
        for s in students:
          s[5]=s[2]+s[3]+s[4]
          s[6]=s[5]/3
    else:
      print("찾는 학생이 없습니다.")

  if choice =='4':
    print("[ 학생성적검색 ]")
    search = input("찾는 학생 이름을 검색해주세요")
    if s[1] == search:
      print("찾는 학생이 있습니다.")
      for s in students:
        print(s)
    else:
      print("찾는 학생이 없습니다.")


  if choice =='5':
    print("[ 학생성적삭제 ]")


  if choice =='6':
    print("[ 등수처리 ]")       


  if choice =='0':
    print("프로그램을 종료합니다.")
    break