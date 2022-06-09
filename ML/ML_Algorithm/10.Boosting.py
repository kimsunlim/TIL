
##Ensemble Boosting 부스팅

#약한학습기를 순차적으로 학습시켜 예측하고 잘못예측한 데이터에 가중치를 부여하여 오류를 개선해나가는 모델이다.
#순차적인 직렬식 앙상블

######Ada Boosting

###분류

import pandas as pd
data=pd.read_csv('breast_cancer_wisconsin.csv',encoding='utf-8')

X=data[data.columns[1:10]]
y=data["Class"]


#분리
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test =train_test_split(X,y, stratify=y, random_state=42)

#정규화
from sklearn.preprocessing import MinMaxScaler 
scaler=MinMaxScaler()

scaler.fit(X_train)
X_scaled_train=scaler.transfrom(X_train)
X_scaled_test =scaler.transform (X_test)


### ada boosting 분류 모델 적용
#n_estimator=100 수행횟수 100번

from sklearn.ensemble import AdaBoostClassifier 
model=AdaBoostClassifier(n_estimator=100, random_state=10)
model.fit(X_scaled_train, y_train)

pred_train=model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)

#정확도 100 > 과대적합

pred_test=model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)

#정확도 95 


##혼동행렬

from sklearn.metrics import confusion_matrix 
confusion_train =confusion_matrix(y_train, pred_train)
print(confusion_train)


##분류리포트

from sklearn.metrics import classification_report
cfreport_train = classification_report(y_train, pred_train)




########GradientBoosting

## 분류

from sklearn.ensemble import GradientBoostingClassifier 
model=GradientBoostingClassifier(n_estimator=100, learning_rate=10, max_depth=1, random_state=0)
model.fit(X_scaled_train, y_train)

pred_train=model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)

#정확도 100 > 과대적합

pred_test=model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)

#정확도 96 


##혼동행렬

from sklearn.metrics import confusion_matrix 
confusion_train =confusion_matrix(y_train, pred_train)
print(confusion_train)


##분류리포트

from sklearn.metrics import classification_report
cfreport_train = classification_report(y_train, pred_train)



#####오류를 찾아 해결하는 방식이므로 훈련데이터에 과대적합되는 경향을 보임
#훈련데이터에서는 과적합나왔지만 테스트데이터에서는 일반적인 경향보임





######Ada Boosting

###회귀

import pandas as pd 
data2= pd.read_csv('house_price.csv',encoding='utf-8')
X=data2[data2.columns[1:5]]
y=data2[['house_value']]



#분리
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test =train_test_split(X,y, random_state=42)

#정규화
from sklearn.preprocessing import MinMaxScaler 
scaler=MinMaxScaler()

scaler.fit(X_train)
X_scaled_train=scaler.transfrom(X_train)
X_scaled_test =scaler.transform (X_test)

##회귀모델 적용

from sklearn.ensemble import AdaBoostRegressor 
model=AdaBoostRegressor(random_state=0, n_estimators=100)
model.fit(X_scaled_train, y_train)
pred_train= model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)

#43.5%


model.fit(X_scaled_test, y_test)
pred_test= model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)
#43%

##RMSE

import numpy as np

from sklearn.metrics import mean_squared_error

MSE_train= mean_squared_error(y_train, pred_train)
MSE_test= mean_squared_error(y_test, pred_test)


########GradientBoosting

## 회귀

from sklearn.ensemble import GradientBoostingRegressor
model=GradientBoostingRegressor(random_state=0)

model.fit(X_scaled_train, y_train)
pred_train= model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)

#61%


model.fit(X_scaled_test, y_test)
pred_test= model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)
#59%

##RMSE

import numpy as np

from sklearn.metrics import mean_squared_error

MSE_train= mean_squared_error(y_train, pred_train)
MSE_test= mean_squared_error(y_test, pred_test)

print(np.sqrt(MSE_train))
