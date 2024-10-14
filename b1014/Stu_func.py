def stu_input(stuNo,students):
  while True:
    no = stuNo + 1
    print("no : ",no)
    name = input(f"{no}번째 학생이름을 입력하세요.(0.이전페이지 이동)")
    if name == '0':
      break
    students.append({"no":no,"name":name})
    stuNo += 1
    return stuNo