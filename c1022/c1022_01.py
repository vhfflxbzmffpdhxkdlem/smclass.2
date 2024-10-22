import requests
from bs4 import BeautifulSoup

url="https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  # 에러시 종료
# print(res.text)

# 태그를 활용한 검색방법
# find,find_all, <-> select_one,select


soup= BeautifulSoup(res.text,"lxml")
# print(soup.find("h2",{"class":"rankingnews_tit"}).text)
# print(soup.select_one("h2.rankingnews_tit").text)
# print(soup.select_one("div#header"))


# select,select_one 사용
data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div")
news = data.select_one("div.rankingnews_box")
print("언론사이름 : ",news.select_one("strong.rankingnews_name").text)
news_lists = news.select("ul.rankingnews_list>li")

for i,datas in enumerate(data):
  print("언론사이름 : ",news.select_one("strong.rankingnews_name").text)
  for idx,news_list in enumerate(news_lists):
    print(f"{idx+1} : ",news_list.select_one("div.list_content>a").text)













h = soup.select_one("div.rankingnews_box")
hl = soup.select_one("div.rankingnews_box").select_one("strong.rankingnews_name").text
hn = h.select_one("ul.rankingnews_list").select_one("div.list_content").next.next.text
# print(hn)





# htm,css 파싱이 되어서 이쁘게 출력
# print(soup.prettify())