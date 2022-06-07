
# 투표기반 앙상블 voting ensemble 
# 여러 분류기를 학습 시킨 후 각각의 분류기가 예측하는 레이블 범주가 가장 많이 나오는 범주를 예측 하는 방법

# 개별 분류기의 최적 하이퍼파라미터를 찾은후 > 투표기반 앙상블로 모델 만듬 



###############분류
##강한 학습기 hardleaner :범주기반 

# 학습기 : 랜포, 로지스틱, 서포트



import pandas as pd

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


#모델 적용 

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier 

#모델 변수 설정
logit_model =LogisticRegression(random_state=42)
rnf_model=RandomForestClassifier(random_state=42)
svm_model= SVC (random_state=42)


#보팅알고리즘 
voting_hard = VotingClassifier(
    estimators=[('Ir', logit_model), ('rf', rnf_model), ('svc', svm_model)],
    voting='hard')

voting_hard.fit(X_scaled_train, y_train)


from sklearn.metrics import accuracy_score 

for clf in (logit_model,rnf_model,svm_model, voting_hard):
    clf.fit(X_scaled_train, y_train)
    y_pred = clf.predict(X_scaled_test)
    print(clf.__class__.name__, accuracy_score(y_test, y_pred))



## 3개의 개별모델과 1개의 투표 앙상블 결과를 적용
#로지 95 랜포 96 서포트 96 앙상블 96 으로 나옴


#혼동행렬

#로지스틱
from sklearn.metrics import confusion_matrix 
log_pred_train =logit_model.predict(X_scaled_train)
log_confusion_train= confusion_matrix(y_train, log_pred_train)
print(log_confusion_train)

log_pred_test =logit_model.predict(X_scaled_test)
log_confusion_test= confusion_matrix(y_test, log_pred_test)
print(log_confusion_test)



#서포트 벡터머신

from sklearn.metrics import confusion_matrix 
svm_pred_train =svm_model.predict(X_scaled_train)
svm_confusion_train= confusion_matrix(y_train, svm_pred_train)
print(svm_confusion_train)

svm_pred_test =svm_model.predict(X_scaled_test)
svm_confusion_test= confusion_matrix(y_test, svm_pred_test)
print(svm_confusion_test)


#랜덤포레스트
from sklearn.metrics import confusion_matrix 
rnd_pred_train =rnf_model.predict(X_scaled_train)
rnd_confusion_train= confusion_matrix(y_train, rnd_pred_train)
print(rnd_confusion_train)

rnd_pred_test =rnf_model.predict(X_scaled_test)
rnd_confusion_test= confusion_matrix(y_test, rnd_pred_test)
print(rnd_confusion_test)

#보팅 앙상블

voting_pred_train =voting_hard.predict(X_scaled_train)
voting_confusion_train= confusion_matrix(y_train, voting_pred_train)
print(voting_confusion_train)

voting_pred_test =voting_hard.predict(X_scaled_test)
voting_confusion_test= confusion_matrix(y_test, voting_pred_test)
print(voting_confusion_test)



###약한 학습기 softleaner :확률기반




import pandas as pd

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


#모델 적용 

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier 

#모델 변수 설정
logit_model =LogisticRegression(random_state=42)
rnf_model=RandomForestClassifier(random_state=42)
svm_model= SVC (random_state=42)




#보팅알고리즘 
voting_soft = VotingClassifier(
    estimators=[('Ir', logit_model), ('rf', rnf_model), ('svc', svm_model)],
    voting='soft')

voting_soft.fit(X_scaled_train, y_train)


from sklearn.metrics import accuracy_score 

for clf in (logit_model,rnf_model,svm_model, voting_soft):
    clf.fit(X_scaled_train, y_train)
    y_pred = clf.predict(X_scaled_test)
    print(clf.__class__.name__, accuracy_score(y_test, y_pred))
    
    
##혼동행렬 보팅만 확인

voting_pred_train =voting_soft.predict(X_scaled_train)
voting_confusion_train= confusion_matrix(y_train, voting_pred_train)
print(voting_confusion_train)

voting_pred_test =voting_soft.predict(X_scaled_test)
voting_confusion_test= confusion_matrix(y_test, voting_pred_test)
print(voting_confusion_test)



##########회귀

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



##개별모델 임포트

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingRegressor


#모델 변수 설정
linear_model =LinearRegression()
rnf_model=RandomForestRegressor(random_state=42)

#보팅알고리즘 
voting_regressor = VotingRegressor(
    estimators=[('Ir', linear_model), ('rf', rnf_model)])
    

voting_regressor.fit(X_scaled_train, y_train)
pred_train=voting_regressor.predict(X_scaled_train)
voting_regressor.score(X_scaled_train, y_train)
#79%


pred_test=voting_regressor.predict(X_scaled_test)
voting_regressor.score(X_scaled_test, y_test)


#Rmse

import numpy as np

from sklearn.metrics import mean_squared_error 
MSE_train= mean_squared_error(y_train, pred_train)
MSE_test= mean_squared_error(y_test, pred_test) 


print(np.sqrt(MSE_train))
print(np.sqrt(MSE_test))












