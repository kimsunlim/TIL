
##서포트 벡터 머신 SVM

#뛰어난 성능 활용도가 높은 분류 모델
#복잡한 과제에 적합한 머신런이 모델
# 레이블 범주를 선형, 비선형, 선, 초평면을 찾느것이 핵심

#어떻게 집단을 분류하는 선을 긋는것이 최선일까를 찾는문제  >멀리, 확실하게 분리할것

#그러나 완벽한 분류는 없기에 어느정도 오류를 허용하는것이 소프트 마진
#파라미터값 조정 >값이 크면 마진폭이 좁아져 과대적합, 값이 작아지면 마진폭이 커져 과소적합



#서포트벡터머신 분류

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

#서포트 벡터머신 분류 모델적용

from sklearn.svm import SVC 
model=SVC()
model.tit (X_scaled_train, y_train)
pred_train= model.predict(X_scaled_train)
model.score(X_scaled_train,y_train)

#98%정확도

pred_test=model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)

#96%정확도


##혼동행렬로 확인
from sklearn.metrics import confusion_matrix 
confusion_train= confusion_matrix(y_train, pred_train)
#정상 4명이 오분류, 환자 4명이 오분류 

confusion_test= confusion_matrix(y_test, pred_test)
#정상 5명 환자 1명이 오분류

#분류예측리포트 

from sklearn.metrics import classification_report 
cfreport_train= classification_report (y_train, pred_train)
#98%,98%

cfreport_test= classification_report (y_test, pred_test)
#92%98%


#모델 튜닝

#그리드탐색

param_grid =[{'kernel':['rbf'],'C':[0.001, 0.01, 0.1, 1, 10, 100],
              'gamma':[0.001,0.01,0.1,1,10,100]},
             {'kernel':['linear'],'C':[0.001, 0.01, 0.1, 1, 10, 100],
             'gamma':[0.001,0.01,0.1,1,10,100]}]
              
              
              
              
from sklearn.model_selection import GridSearchCV 
grid_search= GridSearchCV(SVC(),param_grid, cv=5)
grid_search.fit(X_scaled_train, y_train)

print('best parameter:{}'.format(grid_search.best_params_)) 
print('best score:{:4f}'.format(grid_search.best_score_))  
print('testset score:{:4f}'.format(grid_search.score(X_scaled_test, y_test))) 

#c 100, gamma 0.01 , kernel rbf 일때 최적 
# 97%, 95%정확도나옴



#랜덤탐색 

from scipy.stats import randint 

param_distribs ={'kernel':['rbf'],'C': randint(low=0.001, high=100),
              'gamma': randint (low=0.001, high=100)}
                 
                 


from sklearn.model_selection import RandomizedSearchCV 
random_search=RandomizedSearchCV(SVC(), param_distributions=param_distribs, n_iter=100, cv=5)
random_search.fit(X_scaled_train, y_train)
            
print('best parameter:{}'.format(random_search.best_params_)) 
print('best score:{:4f}'.format(random_search.best_score_))  
print('testset score:{:4f}'.format(random_search.score(X_scaled_test, y_test))) 


#C 19, gamma 5, kernel rbf 일때 최적 
#96%, 96% 정확도

# kernel 종류, c와 gamma등 하이퍼파라미터가 다양함
#모델의 유연성이 뛰어남 





#서포트 벡터 머신 회귀
#kernel=poly가 상식적인 수준으로 정확도가 나옴 그래서 설정할것!

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

#서포트 벡터 머신 회귀 모델 적용

from sklearn.svm import SVR
model=SVR(kernel='poly')
model.fit(X_scaled_train, y_train)
pred_train= model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)

#45% 

pred_test=model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)

#46% 

##RSME확인

import numpy as np
from sklearn.metrics import mean_squared_error

#오차 훈련데이터
MSE_trian=mean_squared_error(y_train,pred_train) #70
MSE_test=mean_squared_error(y_test,pred_test)  #69







#모델 튜닝

#그리드탐색

param_grid ={'kernel':['poly'],'C':[ 0.01, 0.1, 1, 10],
              'gamma':[0.01,0.1,1,10]}
      
                                                     
from sklearn.model_selection import GridSearchCV 
grid_search= GridSearchCV(SVR(kernel='poly'),param_grid, cv=5)
grid_search.fit(X_scaled_train, y_train)

print('best parameter:{}'.format(grid_search.best_params_)) 
print('best score:{:4f}'.format(grid_search.best_score_))  
print('testset score:{:4f}'.format(grid_search.score(X_scaled_test, y_test))) 

#c 10, gamma 10  일때 최적 
# 48%, 51%정확도나옴



#랜덤탐색 

from scipy.stats import randint 

param_distribs ={'kernel':['poly'],'C': randint(low=0.01, high=10),
              'gamma': randint (low=0.01, high=10)}
                 
                 
from sklearn.model_selection import RandomizedSearchCV 
random_search=RandomizedSearchCV(SVR(kernel='poly'), param_distributions=param_distribs, n_iter=20, cv=5)
random_search.fit(X_scaled_train, y_train)
            
print('best parameter:{}'.format(random_search.best_params_)) 
print('best score:{:4f}'.format(random_search.best_score_))  
print('testset score:{:4f}'.format(random_search.score(X_scaled_test, y_test))) 

#c 5, gamma 9  일때 최적 
# 45%, 48%정확도나옴 좋은 성능은 아님





##서포트 벡터머신의 회귀는 kernel에 민감함
















