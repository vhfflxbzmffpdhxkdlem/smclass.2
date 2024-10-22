import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  # 에러시 종료

soup= BeautifulSoup(res.text,"lxml")


# 기준점
data = soup.select_one("#container > div.aside > div > div.aside_area.aside_popular")

# 인기검색종목
h3 = data.select_one("h3.h_popular>span").text
print(h3)


# 1,2,3,4,5
sum = 0
pops = data.select("tbody>tr")
for i,pop in enumerate(pops):
  print(pop.select_one(f" tr:nth-child({i+1}) > th > a").text,"\t",pop.select_one(f"tr:nth-child({i+1}) > td:nth-child({2})").text)
  # 합계를 구하시오.
  # sum += pop.select_one("td").text
  sum += int(pop.select_one(f"tr:nth-child({i+1}) > td:nth-child({2})").text.replace(",",""))
  # next_sibling : 형제관계, find_next_sibling : 형제관계중 검색
  sps = pop.select_one("td").find_next_sibling("td").select("span")
  tit = ["변동","변동액"]
  for idx,sp in enumerate(sps):
    print(tit[idx],":",sp.text.strip())
  print("-"*50)
print(f"합계 :{sum:,}")  

  # print("변동 : ",spns.text)
  # print("변동액 : ",spns)