# if - else
#if elif else

# 100,99,98 A+ / # 97,96,95,94 A / # 93,92,91,90 A- 
# # 89,88, B+ / # 87,86,85,84 B / # 83,82,81,80 B- 
# # 79,78, C+ / # 77,76,75,74 C / # 73,72,71,70 C- 
# # 60점대 D / # 60점 미만 F
num = int(input("점수를 입력해주세요."))

# 중첩 if문
score = ""
if 90<= num:
  score = "A"
  if 98<=num:
    score += "+"
  elif 90<=num:
    score += "-"
if 80<= num:
  score = "B"
  if 88<=num:
    score += "+"
  elif 80<=num:
    score += "-"
if 70<= num:
  score = "C"
  if 88<=num:
    score += "+"
  elif 80<=num:
    score += "-"

# if 98<=num<=100:
#   print("A+")
# elif 94<=num:
#   print("A")
# elif 90<=num:
#   print("A-")
# elif 88<=num:
#   print("B+")
# elif 84<=num:
#   print("B")
# elif 80<=num:
#   print("B-")
# elif 78<=num:
#   print("C+")
# elif 74<=num:
#   print("C")
# elif 70<=num:
#   print("C-")
# elif 60<=num:
#   print("D")
# elif num<=59:
#   print("F")
# else:
#   print("오류")


#3,4,5 - 봄, 6,7,8 - 여름, 9.10.11 - 가을, 12,1,2 - 겨울
#그 외 숫자 - 잘목된 월이 입력되었습니다. 출력하시오.
# num = int(input("숫자를 입력해주세요."))
# if 3<=num<=5: #3<=num and 5>=num
#   print("봄 입니다")
# elif 6<=num<=8:
#   print("여름입니다.")
# elif 9<=num<=11:
#   print("가을입니다.")
# elif 12==num or 1<=num<=2 :
#   print("겨울입니다.")
# else:
#   print("잘목된 월이 입력되었습니다.")

# 입력한 숫자가 10보다 작거나, 100보다 클때 정답입니다. 오답입니다.
# num = int(input("숫자를 입력하세요."))
# if 10>=num or 100<=num:
#   print("정답입니다.")
# else:
#   print("오답입니다.")

# 입력한 숫자가 1보다 크거나 같고 10보다 작거나 같을때만 정답입니다. 오답입니다.
#1<= x <= 10
# num = int(input("숫자를 입력해주세요."))
# if (num>=1)and(num<=10):
#   print("정답입니다.")
# else:
#   print("오답입니다.")

# if 1<=num<=10:
#   print("정답입니다.")
# else:
#   print("오답입니다.")


#  # 입력한 숫자가 짝수인지, 홀수인지 출력하시오.
# num = int(input("숫자를 입력해주세요."))
# if num%2 ==0:
#   print("짝수입니다.")
# else:
#   print("홀수입니다.")