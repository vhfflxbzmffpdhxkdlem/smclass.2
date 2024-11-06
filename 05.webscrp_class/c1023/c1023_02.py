# 파일저장 = txt.csv
import csv

st_list = ['N', '종목명', '현재가', '전일비', '등락률', '거래량', '거래대금', '매수호가', '매도호가', '시가총액', 'PER', 'ROE']
sto_list = ['1', 'KODEX 200선물인버스2X', '2,275', '보합0', '0.00%', '72,439,213', '164,495', '2,260', '2,265', '13,140', 'N/A', 'N/A']
sto_list2 = ['2', 'KODEX 코스닥150선물인버스', '3,840', '상승\n35', '+0.92%', '14,888,627', '56,883', '3,815', '3,820', '2,757', 'N/A', 'N/A']
# csv파일저장 - 리스트 바로 저장
# csv파일로 저장시 한글인코딩 : utf-8-sig
with open('c1023/a.csv','w',encoding='utf-8-sig',newline='')as f:
  writer = csv.writer(f)
  writer.writerow(st_list)
  writer.writerow(sto_list)
  writer.writerow(sto_list2)



print("완료")
f.close()