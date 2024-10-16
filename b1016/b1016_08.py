# sm.shop 한번더만들어 보기

#member
# 로그인

# 상품
# 산 상품 출력


member = [
  {"id":"aaa","pw":"1111","name":"홍길동","nicName":"길동스","abrrss":"서울특별시","money":1000000},
  {"id":"bbb","pw":"2222","name":"유관순","nicName":"관순스","abrrss":"부산관역시","money":2000000},
  {"id":"ccc","pw":"3333","name":"이순신","nicName":"순신스","abrrss":"울산광역시","money":500000},
  {"id":"ddd","pw":"4444","name":"강감찬","nicName":"감찬스","abrrss":"대전광역시","money":100000}
]

product = [
  {"pno":"c01","pName":"닭고기","price":10000},
  {"pno":"d01","pName":"오리고기","price":20000},
  {"pno":"p01","pName":"돼지고기","price":35000},
  {"pno":"m01","pName":"소고기","price":100000}
]
buy_title = ["no","pno","pName","price"]
cart = []
### 함수선언 ###
# 상품 구매
def buy_p(choice,no):
  print(f"{product[choice-1]['pName']}를 구매하셨습니다.")
  c = {"no":no+1,"pno":product[choice-1]["pno"],"pName":product[choice-1]["pName"],"price":product[choice-1]["price"]}
  cart.append(c)
  m['money'] -= product[choice-1]['price']
  no += 1
#------------------
# 구매목록 출력
def output(no):
  print(f"{buy_title[0]}\t{buy_title[1]}\t{buy_title[2]:10}\t{buy_title[3]}")
  print("-"*50)
  sum = 0
  for c in cart:
    sum += c['price']
    print(f"{c['no']}\t{c['pno']}\t{c['pName']:10}\t{c['price']}")
  print(f"총 구매 금액 : {sum:,}")
  print(f"총 구매 건수 : {len(cart)}")




flag = 0
while True:
  mid = input("아이디를 입력해주세요.")
  if mid == '0':
    print("프로그램 종료")
    break
  mpw = input("패스워드를 입력해주세요.")
  for m in member:
    if m['id'] == mid and m['pw'] == mpw:
      while True:
        print("                            [sm shop]")
        print(f"                                          닉네임:{m['nicName']}")
        print(f"                                        보유금액:{m['money']:,}")
        print("1. 닭고기 - 10,000")
        print("2. 오리고기 - 20,000")
        print("3. 돼지고기 - 35,000")
        print("4. 소고기 - 100,000")
        print("9. 구매목록")
        print("0. 로그아웃")
        choice = int(input("원하시는 번호를 입력해주세요"))
        if choice == 1:
          buy_p(choice,no)
        elif choice == 2:
          buy_p(choice,no)
        elif choice == 3:
          buy_p(choice,no)
        elif choice == 4:
          buy_p(choice,no)
        elif choice == 9:
          output(no)

        elif choice == 0:
          print("로그아웃")
          break

      flag = 1
  if flag == 0:
    print("아이디 혹은 비밀번호가 잘못입력되었습니다. 다시 입력해주세요")