import os

def getDataList(folder, ext):
    tmpList = os.listdir(folder)
    ret = list()
    for tmp in tmpList:
        if ('.' + ext == os.path.splitext(tmp)[1]):
            ret.append(tmp)
    return ret

#folder = './preData/'
#folder = '../data/classifed/'
folder = '../data/'
fileName = 'dataList.txt'

li = getDataList(folder, 'csv')
f = open(fileName, 'w')

for i in li:
    print (i)
    f.write(i + '\n')

f.close()