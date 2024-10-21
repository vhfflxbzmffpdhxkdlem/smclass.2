# naver 파일저장. 리솜리조트 파일 저장


# url = [
#   "http://www.google.com"
#   "http://www.naver.com"
#   "http://www.daum.net"
# ]

# url = [
#   "http://www.coupang.com/"
# ]

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
# for i in range(len(url)):
#   res = requests.get(url[i],headers=headers)
#   res.raise_for_status() # 정상코드


# # 웹소스 파일 저장
# with open("c1021/{i}.html","w",encoding="utf-8") as f:
#   f.write(res.text)

# print("프로그램 종료!")

# 쿠팡페이지 저장
import requests
url = "http://www.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 정상코드
print(res.text)