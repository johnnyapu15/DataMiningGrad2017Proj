#20171210 Johnnyapu15
#-*- coding:utf-8 -*-
#데이터를 실질적으로 분류 처리
#csv 데이터를 읽고 shingle-기준에 의해 분류

import listModule as LM
from shingle import *
import itertools

ATTRIBUTE = ['Date','Open','High','Low','Close','Adj Close','Volume']
#Date,Open,High,Low,Close,Adj Close,Volume
LM.init()

def getValList(code, attrName, cmpBase):
    tmpKOSPIData = LM.csv.reader(open(LM.dataPath + code))
    tmpValueList = []
    tmpIdx = ATTRIBUTE.index(attrName)
    for val in tmpKOSPIData:
        tmpValueList.append(val[tmpIdx])
    return tmpValueList

def getClosePerOpen(code, cmpBase):
    tmpKOSPIData = LM.csv.reader(open(LM.dataPath + code))
    tmpValueList = []
    KOSPIDataList = list(tmpKOSPIData)[1:]
    for idx, val in enumerate(KOSPIDataList):

        tmpPer = ((float(val[4]) - float(val[1]))/float(val[1]))
        if tmpPer > float(cmpBase):
            tmp = []
            tmpI = 0
            if (idx - LM.N >= 0):
                tmpI = idx - LM.N
                for i in range(tmpI, idx + 1):
                    tmp.append(KOSPIDataList[i])
                tmpValueList.append(tmp)
            else:
                tmpI = 0
            
    return tmpValueList
