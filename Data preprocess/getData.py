#-*- coding:utf-8 -*-

import listModule

listModule.init()

df = listModule.data.DataReader(
    listModule.KOSPI,
    "yahoo",
    listModule.START
)

#Save to csv file
df.to_csv(listModule.preDataPath + 'KOSPI.csv')

KOSPIList = listModule.getKOSPIList()
gotList = []
#All of KOSPI, Get the all of data since 1996, KOSPI.

for li in KOSPIList[1:]:
    print(li)
    try:
        tmpDf = listModule.data.DataReader(
            li,
            'yahoo',
            listModule.START
        )
    except listModule._utils.RemoteDataError  as RDE:
        print("ERROR with " + li + ": " + RDE)
        continue
        pass
    else:
        tmpDf.to_csv(listModule.dataPath + li + '.csv')
        gotList.append(li + '.csv')
    

wtr = listModule.csv.writer(open(listModule.dataPath + 'downloadedList.csv', 'w'))
for dl in gotList:
    wtr.writerow(dl)