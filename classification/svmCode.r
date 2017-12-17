#Johnnyapu15 20171216 SVM in R

#predict set은 y를 포함하지 않아야한다.
#training시 각종 factor들의 level을 미리 total set으로 설정해주고 시작할 것.

library(e1071)

classList = c(
    rep('factor', 6),
    rep('numeric', 3),
    'logical',
    rep('numeric', 5),
    rep('factor', 2)
)

classList2 = c(
    rep('factor', 5),
    rep('numeric', 3),
    'logical',
    rep('numeric', 3)
)

prep = read.csv('data/svmData/preprocess.csv', encoding='utf-8', colClasses = c(rep('factor', 4)))



ages = c('All', '20', '30', '40', '50', '60')
i = 1
SVMF = function(k){
    i=1
    for (age in ages){

        tmpD = read.csv(paste('data/svmData/train-data-',age,'-k=',k,'.csv',sep=''), colClasses=classList)

        datTmp = tmpD[c(5:13,15)]
        datTmp[is.na(datTmp)] = 0
        
        levels(datTmp$dong) = levels(prep$dong)
        levels(datTmp$code) = levels(prep$code)

        model = svm(pt~., datTmp, type = 'eps-regression')

        write.svm(model, paste('data/svmData/result/svmModel-',age,sep=""))
        
        tmpTr = read.csv(paste('data/svmData/predictor/predictor-',age,'.csv',sep=''), colClasses=classList2)
        datTmp2 = tmpTr[c(4:12)]
        datTmp2[is.na(datTmp2)] = 0
    
        levels(datTmp2$dong) = levels(prep$dong)
        levels(datTmp2$code) = levels(prep$code)

        svmPredicted = predict(model, datTmp2)
        
        write.csv(cbind(tmpTr, svmPredicted), paste('data/svmData/result/validation-',age,'.csv',sep=''))

        i = i + 1
    }
}

svmfunc = function(){
    tmpD = read.csv('data/svmData/train-data-20-k=5.csv', colClasses=classList)
    datTmp = tmpD[c(2:13,15)]
    datTmp[is.na(datTmp)] = 0

    model20 = svm(pt~., datTmp, type = 'eps-regression')

    tmpD = read.csv('data/svmData/train-data-30-k=5.csv', colClasses=classList)
    datTmp = tmpD[c(2:13,15)]
    datTmp[is.na(datTmp)] = 0

    model30 = svm(pt~., datTmp, type = 'eps-regression')

    tmpD = read.csv('data/svmData/train-data-40-k=5.csv', colClasses=classList)
    datTmp = tmpD[c(2:13,15)]
    datTmp[is.na(datTmp)] = 0

    model40 = svm(pt~., datTmp, type = 'eps-regression')

    tmpD = read.csv('data/svmData/train-data-50-k=5.csv', colClasses=classList)
    datTmp = tmpD[c(2:13,15)]
    datTmp[is.na(datTmp)] = 0

    model50 = svm(pt~., datTmp, type = 'eps-regression')

    tmpD = read.csv('data/svmData/train-data-60-k=5.csv', colClasses=classList)
    datTmp = tmpD[c(2:13,15)]
    datTmp[is.na(datTmp)] = 0

    model60 = svm(pt~., datTmp, type = 'eps-regression')

    tmpD = read.csv('data/svmData/train-data-All-k=5.csv', colClasses=classList)
    datTmp = tmpD[c(2:13,15)]
    datTmp[is.na(datTmp)] = 0

    modelAll = svm(pt~., datTmp, type = 'eps-regression')
    


    for (age in ages){

    }
}


loadModel = function(){

    m20 = read.svm('data/svmData/result/svmModel-20)')
    
    
}


for (age in ages){
    
    data = dataOfDong(age, '총', pd)

    write.csv(file=paste('data/svmData/predictor/predictor-',age,'.csv',sep=''), x=data)
}