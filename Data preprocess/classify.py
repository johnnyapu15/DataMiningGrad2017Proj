#20171210 Johnnyapu15
#-*- coding:utf-8 -*-
#데이터를 실질적으로 분류 처리,
#학습 데이터를 만듦.
#csv 데이터를 읽고 shingle-기준에 의해 분류

import listModule as LM
from shingle import *
import classifyAndSaveModule as CLA 
import datetime

def cmp0(a):
    return 1

def cmp1(a):
    return (a > LM.A)

def cmp2(a):
    return (a < LM.A)

def cmpPer(_per):
    ret = 'NORMAL'
    if (_per > UPVALUE):
        ret = 'UP'
    elif (_per < DOWNVALUE):
        ret = 'DOWN'
    return ret
def retPer(_per):
    return _per
DAY = ['MON', 'TUE', 'WED', 'THU', 'FRI']
HEADER = ['Date', 'Day', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
HEADERSTR = ''
for i in range(1,15):
    tmpHEADERSTR = ''
    for idx, attr in enumerate(HEADER):
        tmpHEADERSTR += str(attr) + str(i) 
        if idx < len(HEADER) - 1:
            tmpHEADERSTR += ', '
    HEADERSTR += tmpHEADERSTR
    if i < 14:
        HEADERSTR += ','
HEADERSTR += ', Class'
print('HEADER: ' + HEADERSTR)
UPVALUE = .10
DOWNVALUE = -.03
INTERVAL = 14

LM.init()


CLASSIFIEDFOLDER = '../data/classified/'


downloaded = list(LM.csv.reader(open('../data/dataList.txt', 'r')))


LM.N = INTERVAL
allWr = open(CLASSIFIEDFOLDER + 'allValues_volPer100_' + str(LM.N) + '.csv', 'w')
allWr.write(HEADERSTR + '\n')
for idx, li in enumerate(downloaded):
    tmp = CLA.getClosePerOpenAndVol(li[0], retPer)
    for r1 in tmp:
        tmpR = str(r1).replace("'", '').replace('[','').replace(']','')
        allWr.write(tmpR)
        allWr.write('\n')
    print('processing: ' + str(idx) + '/' + str(len(downloaded)))


# LM.A = UPVALUE
# LM.N = INTERVAL

# allWr = open(CLASSIFIEDFOLDER + 'allValues_' + str(LM.A) + '_' + str(LM.N) + '.csv', 'w')
# allWr.write(HEADERSTR + '\n')
# for idx, li in enumerate(downloaded):
#     tmp = CLA.getClosePerOpen(li[0], cmp1)

#     tmpWr = open(CLASSIFIEDFOLDER \
#      + 'up_' + str(LM.A) + '_' + str(LM.N) + li[0], 'w')
#     for r1 in tmp:
#         tmpR = str(r1).replace("'", '').replace('[','').replace(']','')
#         tmpWr.write(tmpR)
#         tmpWr.write('\n')
#         allWr.write(tmpR)
#         allWr.write('\n')
#     print('processing: ' + str(idx) + '/' + str(len(downloaded)))
# LM.A = DOWNVALUE
# LM.N = INTERVAL
# allWr = open(CLASSIFIEDFOLDER + 'allValues_' + str(LM.A) + '_' + str(LM.N) + '.csv', 'w')
# for idx, li in enumerate(downloaded):
#     tmp = CLA.getClosePerOpen(li[0], cmp2)

#     tmpWr = open(CLASSIFIEDFOLDER \
#      + 'down_' + str(LM.A) + '_' + str(LM.N) + li[0], 'w')
#     for r1 in tmp:
#         tmpR = str(r1).replace("'", '').replace('[','').replace(']','')
#         tmpWr.write(tmpR)
#         tmpWr.write('\n')
#         allWr.write(tmpR)
#         allWr.write('\n')
#     print('processing: ' + str(idx) + '/' + str(len(downloaded)))


#When read these things
#for r0 in reader:
#   for r1 in r0:
#       print((r1).replace("'", '').replace('[','').replace(']','').replace(',','').split())

