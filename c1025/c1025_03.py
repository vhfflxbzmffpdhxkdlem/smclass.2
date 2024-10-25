# float타입으로 변경해서 리스트로 저장하시오.
a = ['1만','3,450','1.7만','500','1000']
b = "1.7만"
def chg(val):
  r_val = 0
  if '만' in val: r_val = float(val[:-1])*10000
  else: r_val = float(val.replace(",","")) 
  return r_val

a_list = list(map(chg,a))
print(a_list) 
print(max(a_list)) # 최소값
print(min(a_list)) # 최대값
a_list.sort(reverse=True) # 역순정력
print(a_list)

def asdf(vel):
  r_vel = 0
  if '만' in vel: r_vel = float(vel[:-1])*10000
  else: r_vel = float(vel.replace(",",""))
  return r_vel

c = asdf,b
print(c)


# for i in a:
#   if '만' in i:
#     '만'.[:-1]
#     c = float(i)
#     b.append(c)
#   else:
#     d = float(i)
#     b.append(d)
# print(b)


# a = "1.7"
# if '만' in a:
#   print("있어요")
# else: print("없어요")

# 리스트 + 리스트
# a = [1,2,3]
# b = [4,5,6]
# print(a+b)