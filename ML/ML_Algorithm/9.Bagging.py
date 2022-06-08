
# ensemble  Bagging

# 여러개의 부트스트랩 생성하고 각 부트스트랩 데이터들을 학습시킨 후 결과 투표
# 기본알고리즘 동일한거 씀



#######분류 

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

##배깅 모델 적용
##기본 알고리즘은 SVC

from sklearn.svm import SVC 
from sklearn.ensemble import BaggingClassifier 

#기본 알고리즘 svc적용, 부트스트랩수 10
model = BaggingClassifier (base_estimator=SVC(), n_estimators=10, random_state-0)
model.fit(X_scaled_train, y_train)

pred_train=model.predict(X_scaled_train)
model.score(X_scaled_trian, y_train)
#정확도 98%

pred_test=model.predict(X_scaled_test)
model.score(X_scaled_test,y_test)
#정확도 95% 


##혼동행렬

from sklearn.metrics import confusion_matrix 
confusion_train = confusion_matrix(y_train, pred_trian)
print(confusion_trian)


##분류예측레포트

from sklearn.metrics import classification_report 
cfreport_train = classification_report(y_trian, pred_train)
print(cfreport_train)



############회귀

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


##배깅회귀 적용
#k최근접이웃

from sklearn.neighbors import KNeighborsRegressor 
from sklearn.ensemble import BaggingRegressor 

model = BaggingRegrssor(base_estimaor=KNeighborsRegressor(), n_estimators=10, random_state=0)
model.fit(X_scaled_trian, y_train)
pred_train=model.predict(X_scaled_train)
model.score(X_scaled_train, y_trian)

#69%



pred_test=model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)

#56%


##RSME

import numpy as np
from sklearn.metrics import mean_squared_error

MSE_train =mean_squared_error(y_train, pred_train)
MSE_test =mean_squared_error(y_test, pred_test)


