#20171210 Johnnyapu15

##### Shingling length of data into shingling size
def shingle(_data, _sh_size):
    shingledList = list()
    for i in range(0, len(_data) - _sh_size + 1):
        shingledList.append(_data[i:i + _sh_size])
    return shingledList


