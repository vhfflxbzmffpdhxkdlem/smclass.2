#1759870
#9870
#590
money = int(input("숫자를 입력하세요."))
if money == 1759870:
  print("50000원 개수 : ",money//50000)
  print("10000원 개수 : ",money%50000//10000)
  print("5000원 개수 : ",money%50000%10000//5000)
  print("1000원 개수 : ",money%50000%10000%5000//1000)
  print("500원 개수 : ",money%50000%10000%5000%1000//500)
  print("100원 개수 : ",money%50000%10000%5000%1000%500//100)
  print("50원 개수 : ",money%50000%10000%5000%1000%500%100//50)
  print("10원 개수 : ",money%50000%10000%5000%1000%500%100%50//10)
elif money==9870: #else if
  print("5000원 개수 : ",money%50000%10000//5000)
  print("1000원 개수 : ",money%50000%10000%5000//1000)
  print("500원 개수 : ",money%50000%10000%5000%1000//500)
  print("100원 개수 : ",money%50000%10000%5000%1000%500//100)
  print("50원 개수 : ",money%50000%10000%5000%1000%500%100//50)
  print("10원 개수 : ",money%50000%10000%5000%1000%500%100%50//10)
elif money==590:
  print("500원 개수 : ",money%50000%10000%5000%1000//500)
  print("100원 개수 : ",money%50000%10000%5000%1000%500//100)
  print("50원 개수 : ",money%50000%10000%5000%1000%500%100//50)
  print("10원 개수 : ",money%50000%10000%5000%1000%500%100%50//10)
else:
  print("a는 590이하입니다.")

#str1 = input("문자를 입력하세요.")
#a = len(str1) #문자의 길이 .length

#if a == 5:
#  print("a는 5입니다.")
#elif a==4: #else if
#  print("a는 4입니다.")
#elif a==3:
#  print("a는 3입니다.")
#else:
#  print("a는 2이하입니다.")
 


# money = 1759870
#5만, 1만, 5천, 500원, 100원, 50원, 10원
#print("50000원 개수 : ",money//50000)
#print("10000원 개수 : ",money%50000//10000)
#print("5000원 개수 : ",money%50000%10000//5000)
#print("1000원 개수 : ",money%50000%10000%5000//1000)
#print("500원 개수 : ",money%50000%10000%5000%1000//500)
#print("100원 개수 : ",money%50000%10000%5000%1000%500//100)
#print("50원 개수 : ",money%50000%10000%5000%1000%500%100//50)
#print("10원 개수 : ",money%50000%10000%5000%1000%500%100%50//10)
 
# money = 780
#500 - 1  100 - 2 50 - 1  10 - 3
#print("500원 개수 : ",money//500) 
#print("100원 개수 : ",money%500//100)
#print("50원 개수 : ",money%500%100//50)
#print("10원 개수 : ",money%500%100%50//10)
#print("1원 개수 : ",money%500%100%50%10)