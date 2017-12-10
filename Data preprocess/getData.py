from pandas_datareader import data, wb
from datetime import datetime
import csv

START = datetime(1996, 1, 1)
END = datetime.now()

#A%
A = 25
N = 14

#Pre-data
preDataPath = './preData/'
preData = open(preDataPath + 'preData.csv', 'w')


#KOSPI List
# 1:index 2:종목코드 3:기업명 4:업종코드 5:업종명 6:상장주식수 7:자본금 8:액면가
KOSPIListPath = '../data/KOSPI_LISTED.csv'

kospiFile = open(KOSPIListPath, 'r', encoding='utf-8')
kospiRdr = csv.reader(kospiFile)
kospiList = []

#코스피 종목을 걸러낼 때, 이 for문 안에 if문을 넣어주면 됨.
for li in kospiRdr:
    kospiList.append(li[1])


#KOSPI
KOSPI = '^KS11'

df = data.DataReader(
    "^KS11",
    "yahoo",
    datetime(2017,3,3),
    datetime(2017,3,4)
)

preData.write(df)

#preDataWrtr = csv.writer(preData)
#preDataWrtr.writerow()
