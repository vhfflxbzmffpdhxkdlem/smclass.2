fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
fruits = fruit.split(",")
print(fruits)
print(len(fruits))
# 리스트 인 경우 검색해서 해당되는 index 를 출력하시오.
# 배에 해당되는 index 번호를 출력

search = input("과일 이름을 입력해주세요")
for idx,f in enumerate(fruits):
  if f == search:
    print("해당위치 : ",idx)

# print(fruit.find('배',0))#3
# print(fruit.find('배',fruit.find('배',0)+1))#15
# print(fruit.find('배',fruit.find('배',fruit.find('배',0)+1)+1))#20

# print(fruit.find("딸기",0)) #5
# print(fruit.find("딸기",fruit.find("딸기",0)+1))
# print(fruit.find("딸기",6))
