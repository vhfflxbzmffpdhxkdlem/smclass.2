# 함수선언
def calc(num1,num2,op):
  if op =='+':
    result = num1+num2
  elif op =='-':
    result = num1-num2
  elif op =='*':
    result = num1*num2
  elif op =='/':
    result = num1/num2
  return result
num1 = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))
op = input("+,-,*,/ 하나를 선택하세요")
print("결과값 : ",calc(num1,num2,op))