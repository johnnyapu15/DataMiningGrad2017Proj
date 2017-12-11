#20171210 Johnnyapu15
#-*- coding:utf-8 -*-
#데이터를 실질적으로 분류 처리,
#학습 데이터를 만듦.
#csv 데이터를 읽고 shingle-기준에 의해 분류

import listModule as LM
from shingle import *
import classifyAndSaveModule as CLA 
UPVALUE = .10
DOWNVALUE = -.3
INTERVAL = 14

LM.init()


CLASSIFIEDFOLDER = '../data/classified/'


downloaded = list(LM.csv.reader(open('../data/downloadedList.csv', 'r')))

LM.A = UPVALUE
LM.N = INTERVAL

for li in downloaded:
    tmp = CLA.getClosePerOpen(li, LM.A)

    tmpWr = LM.csv.writer(open(CLASSIFIEDFOLDER \
     + 'up_' + str(LM.A) + '_' + str(LM.N) + li, 'w'))
    for r1 in tmp:
        tmpWr.writerow(r1)

LM.A = DOWNVALUE
LM.N = INTERVAL

for li in downloaded:
    tmp = CLA.getClosePerOpen(li, LM.A)

    tmpWr = LM.csv.writer(open(CLASSIFIEDFOLDER \
     + 'down_' + str(LM.A) + '_' + str(LM.N) + li, 'w'))
    for r1 in tmp:
        tmpWr.writerow(r1)



#When read this thing
#for r0 in reader:
#   for r1 in r0:
#       print((r1).replace("'", '').replace('[','').replace(']','').replace(',','').split())

