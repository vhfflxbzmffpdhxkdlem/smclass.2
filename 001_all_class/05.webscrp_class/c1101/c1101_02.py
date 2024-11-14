import datetime

# 현재년도
print(datetime.datetime.now().year)
nowYear = datetime.datetime.now().year
in_year = "20020312"
print(in_year)
# print(nowYear-int(in_year[:4]))
print(f"현재 나이 : {nowYear-int(in_year[:4])}")

