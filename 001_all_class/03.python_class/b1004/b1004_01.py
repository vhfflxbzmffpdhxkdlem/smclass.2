students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]

# 합계, 평균 출력해서 전체를 출력하시오.
# 1 홍길동 100 90 99 289 96.33

for s in students:
  total = s[2]+s[3]+s[4]
  avg = total/3
  s.append(total)
  s.append(avg)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))

search = input("이름을 입력해주세요")

for s in students:
  count = 0
  if s[1] == search:
    print(s)
    count == 1
    break
if count == 0:
  print("찾으시는 이름이 없습니다.")

  # 합계,평균 추가해서 전체를 출력하시오.
# for s in students:
#   s.append(s[2]+s[3]+s[4])
#   s.append((s[2]+s[3]+s[4])/3)
# print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
# print("-"*55)
# for s in students:
#   print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}")