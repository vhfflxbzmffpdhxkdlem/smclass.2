import
lotto = [1]*3+[0]*6
a_list = [
  [1,0,0],
  [0,1,0],
  [0,0,1]
]
aa_list = [
  ["로또","로또","로또"]
  ["로또","로또","로또"]
  ["로또","로또","로또"]
]
for i in range(3):
  for j in range(3):
    a_list[i][j] = lotto[i*3+j]

while True:
  my_money = int(input("얼마를 투자하시겠습니까?"))
  print("\t0\t1\t2")
  print("-"*30)
  print()
  for i in range(3):
    print(i,end="\t")
    for j in range(3):
      print(aa_list)
      num = input("원하시는 곳을 선택해주세요(0.0)")
      num2 = num.split(".")
      if a_list[int(num2[0])][int(num2[1])] == 1:
        aa_list[int(num2[0])][int(num2[1])] == "당첨"
        print(f"{[int(num2[0])][int(num2[1])]}당첨금 : ",)