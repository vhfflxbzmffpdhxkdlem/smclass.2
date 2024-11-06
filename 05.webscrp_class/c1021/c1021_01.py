# 웹스크래핑 세팅
import requests
# res = requests.get("http://www.google.com/") # html 소스코드 가져온다
res = requests.get("http://www.naver.com/") # html 소스코드 가져온다
# res = requests.get("http://www.melon.com/index.htm") # html 소스코드 가져온다
res.raise_for_status()  # 에러시 종료

# resquests 정보를 가져올시 
# 제이쿼리,자비그크립트,외부페이지,react,vue.. 비동기식으로 작동되는 소스는 
# 가져오지 못함.

print("총 문자 길이 : ",len(res.text))





# print(res.text) # html 소스 출력

# 웹소스 파일 저장
# f = open("a.ahtl","w",encoding="utf-8")
# f.write(res.text)
# f.close()


# f.close()
# with open("c1021/a.html","w",encoding="utf-8") as f:
#   f.write(res.text)

# if res.status_code == 200:
#   print(res.text)
# else: print("접근할수 없습니다.")

# print("응답코드 : ",res.status_code)  #  200

# print(res.text)

