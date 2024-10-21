# import S_func
from S_func import *
#--------------------------
# 함수외부분리
#--------------------------


#-----------------------프로그램 시작-------------------------------#
# 학생성적프로그램
while True:
  choice = title_program()       # 메뉴출력함수 호출
  if choice == "1":              
    stuNo = stu_input()     # 학생성적입력함수 호출
  elif choice == "2":
    stu_output()         # 학생성적출력함수 호출
  elif choice == "3":
    stu_update()         # 학생성적수정함수 호출
  elif choice == "4":
    stu_selsct()         # 학생성적검색함수 호출
  elif choice == "5":   
    stu_delete()         # 학생성적삭제함수 호출
  elif choice == "6":
    stu_rank()                   # 학생성적등수처리함수 호출
  elif choice == "7":
    stu_sort()                   # 학생성적정렬함수 호출
  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break
# 학생성적 입력부분을 구현하시오.
# dict타입으로 입력을 할것
# 번호,이름,국어,영어,수학,합계,평균,등수
# 입력이 완료되면 출력이 바로 되도록 하시오.