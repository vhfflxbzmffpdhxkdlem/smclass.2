member = [
  {"id":"aaa","pw":"1111","name":"홍길동","nicName":"길동스","address":"서울시","money":1000000000},
  {"id":"bbb","pw":"2222","name":"유관순","nicName":"관순스","address":"부산시","money":70000000},
  {"id":"ccc","pw":"3333","name":"이순신","nicName":"순신스","address":"경기도","money":50000000},
  {"id":"ddd","pw":"4444","name":"강감찬","nicName":"감찬스","address":"인천시","money":10000000},
  {"id":"eee","pw":"5555","name":"김구","nicName":"구스","address":"대구시","money":20000000}
]

#member.txt 파일생성새서 csv형태로 문자열로 저장하시오.

f = open('member.txt','w',encoding='utf-8')
for m in member:
  f.write(f"{m['id']},{m['pw']},{m['name']},{m['nicName']},{m['address']},{m['money']}\n")
f.close()

# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
#   {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
#   {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
#   {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
#   {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
# ]
# students 딕셔너리파일을 메모장에 csv파일형태로 저장하시오.

# f = open('students.txt','w',encoding='utf-8')
# for s in students:
#   f.write(f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n")
# f.close()


# f = open('students.txt','w',encoding='utf-8')
# f.write("1. 홍길동,100,100,99,299,99.67,0\n")
# f.write("2,유관순,80,80,99,259,86.33,0\n")
# f.write("3,이순신,100,99,90,289,96.33,0\n")
# f.close()

# studebts,txt
#   [1,"홍길동",100,100,99,299,99.67,0],
#   [2,"유관순",80,80,99,259,86.33,0],
#   [3,"이순신",100,99,90,289,96.33,0]



# a = ["no","name","kor","eng"]
# b = [1,"홍길동",100,100]
# print(dict(zip(a,b)))

# a = ["홍길동","유관순","이순신"]
# b = [100,90,80]
# c = zip(a,b)
# # print(list(c))
# print(dict(c))