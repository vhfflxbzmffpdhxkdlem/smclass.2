students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]


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
    print(s)
  