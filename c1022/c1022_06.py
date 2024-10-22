import requests
from bs4 import BeautifulSoup

url="https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  # 에러시 종료

soup= BeautifulSoup(res.text,"lxml")

f = open('c1022/melron.txt','w',encoding='utf-8')
# 순위,사진링크주소,제목,가수명

# 기준점
tits = ["순위","곡정보","가수명"]
data = soup.select_one("#frm > div > table")
tis = data.select("tbody > tr.lst50")
lists = data.select("tbody > tr > td")

lis = []



#100위 출력
for i in range(1,2):
  lis = (lists[1].select_one("span").text)
  lis = (lists[3].select_one("img")['src'])
  lis = (lists[5].select_one("span>a").text)

f.write(','.join(lis).join(tits)+"\n")






# print(data.select_one("span.rank").text)






f.close()










