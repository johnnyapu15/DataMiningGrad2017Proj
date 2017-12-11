#-*- coding:utf-8 -*-

from pandas_datareader import data, wb, _utils
from datetime import datetime
import csv
import pickle

global START
global END
global A
global N
global preDataPath
global dataPath
global KOSPIListPath
global KOSPIFile
global KOSPIList
global KOSPI

def init():

    global START
    global END
    global A
    global N
    global preDataPath
    global dataPath
    global KOSPIListPath
    global KOSPIFile
    global KOSPIList
    global KOSPI

    START = datetime(1996, 1, 1)
    END = datetime.now()

    #A%
    A = 25
    N = 14

    #data path
    preDataPath = './preData/'
    dataPath = '../data/'
    #KOSPI List
    # 1:index 2:종목코드 3:기업명 4:업종코드 5:업종명 6:상장주식수 7:자본금 8:액면가
    KOSPIListPath = '../data/KOSPI_LISTED.csv'

    KOSPIFile = csv.reader(open(KOSPIListPath))
    KOSPIList = []

    #KOSPI
    KOSPI = '^KS11'

def getKOSPIList():
    #코스피 종목을 걸러낼 때, 이 for문 안에 if문을 넣어주면 됨.
    for li in KOSPIFile:
        tmpLi = ''
        for i in range(6 - len(str(li[1]))):
            tmpLi += '0'
        tmpLi += str(li[1])
        KOSPIList.append(tmpLi + '.KS')
    return KOSPIList



