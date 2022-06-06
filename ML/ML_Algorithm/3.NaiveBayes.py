

##나이브 베이즈 Naive Bayes
# 사건b가 주어졌을때 사건 A가 일어날 확률 P(A/B)
# 특성치 x를 단순화 하는 것


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

## 나이브 베이즈 분류 모델 적용 

from sklearn.naive_bayes import GaussianNB 
model=GaussianNB()
 
model.fit(X_scaled_train, y_train) #모델 적용
pred_train=model.predict(X_scaled_train) #예측값 
model.score(X_scaled_train, y_train)#정확도  #0.96

pred_test= model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)  #0.95



#혼동행렬
from sklearn.metrics import confusion_matrix
confusion_train = confusion_matrix(y_train,pred_train) ##예측값을 혼동행렬에 넣어줘야함!! 
print('훈련데이터 오차행렬:\n',  confusion_train)

confusion_test = confusion_matrix(y_test,pred_test)

#정상을 예측하는 정확도가 다른 알고리즘에 비해 떨어짐

#분류리포트
from sklearn.metrics import classification_report 
cfreport_train= classification_report(y_train, X_scaled_train)
print('분류리프토:\n',cfreport_train)


cfreport_test = classification_report(y_test,pred_test)


##Grid search
#var_smoothing 을 0~10까지 설정 

param_grid ={'var_smoothing':[0,1,2,3,4,5,6,7,8,9,10]}

from sklearn.model_selection import GridSearchCV
grid_search =GridSearchCV (GaussianNB(), param_grid, cv= 5)
grid_search.fit(X_scaled_train, y_train) 


print('best parameter:{}'.format(grid_search.best_params_)) #0
print('best score:{:4f}'.format(grid_search.best_score_))  #0.9649
print('testset score:{:4f}'.format(grid_search.score(X_scaled_test, y_test))) #0.9591

#하이퍼 파라미터는 var_smoothing가 0일때 최적임 이때 훈련데인터는 96.5퍼 테스트데이터는 95.9퍼


##random search 
# 0~20까지 100번 수행

from scipy.stats import randint

param_distribs  = {'var_smoothing':randint(low=0 , high=20)}

from sklearn.model_selection import RandomizedSearchCV
random_search =RandomizedSearchCV(GaussianNB(), param_distributions=param_distribs, n_iter=100, cv=5)
random_search.fit(X_scaled_train, y_train)


print('best parameter:{}'.format(random_search.best_params_)) #0
print('best score:{:4f}'.format(random_search.best_score_))  #0.9649
print('testset score:{:4f}'.format(random_search.score(X_scaled_test, y_test))) #0.9591


##그리드와 랜덤에서 유사한 결과 나옴 


##회귀

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



##나이브베이즈 회귀 적용

from sklearn.linear_model import BayesianRidge 
model= BayesianRidge()
model.fit(X_scaled_train, y_train)
pred_train=model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)
#0.54

pred_test=model.predixt(X_scaled_test)
model.score(X_scaled_test, y_test)
#0.56


#RSME 

import numpy as np 
from sklearn.metrics import mean_squared_error

MSE_train =mean_squared_error(y_train, pred_train)
MSE_test = mean_squared_error(y_test,pred_test)

print('훈련데이터',np.sqrt(MSE_train)) #64
print('테스트데이터',np.sqrt(MSE_test)) #63 


#그리드 

param_grid ={'alpha_1':[1e-06, 1e-05,1e-04, 1e-03, 1e-02, 1e-01,1,2,3,4],
             'lambda_1':[1e-06, 1e-05,1e-04, 1e-03, 1e-02, 1e-01,1,2,3,4]}

from sklearn.model_selection import GridSearchCV
grid_search =GridSearchCV (BayesianRidge(), param_grid, cv= 5)
grid_search.fit(X_scaled_train, y_train) 


print('best parameter:{}'.format(grid_search.best_params_)) #알파 4, 람다 1e-06일때 최적
print('best score:{:4f}'.format(grid_search.best_score_))  #0.54
print('testset score:{:4f}'.format(grid_search.score(X_scaled_test, y_test))) #0.56

#랜덤서치

from scipy.stats import randint

param_distribs  ={'alpha_1':randint(low=1e-6, high=10), 'lambda_1':randint(low=1e-6, high=10)}
from sklearn.model_selection import RandomizedSearchCV
random_search =RandomizedSearchCV(GaussianNB(), param_distributions=param_distribs, n_iter=100, cv=5)
random_search.fit(X_scaled_train, y_train)


print('best parameter:{}'.format(random_search.best_params_)) #0
print('best score:{:4f}'.format(random_search.best_score_))  #0.54
print('testset score:{:4f}'.format(random_search.score(X_scaled_test, y_test))) #0.56

#그리드와 랜덤 유사한 결과  











