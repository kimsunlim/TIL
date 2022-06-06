

### 인공신경망 ANN

#인공신경망은 input자극과 output반응과의 연관을 구현한 알고리즘
#중간 은닉층과 노드를 두어 특성치로 부터 분류와 회귀 용이
#다층퍼셉트론 수행 / 입력층은 특성치 출력층은 레이블
#은닉층 노드의 개수가 핵심파라미터 



##인공신경망 분류

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

#분류모델적용

from sklearn.neural_network import MLPClassifier
model=MLPClassifier()
model.fit(X_scaled_train, y_train)
pred_train= model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)
#97%

pred_test=model.predict(X_scaled_test)
model.score(X_scaled_test,y_test)
#95%

#오차행렬 확인

from sklearn.metrics import confusion_matrix 
confusion_train = confusion_matrix(y_train, pred_train)
print('훈련데이터:\n',confusion_train)


confusion_test = confusion_matrix(y_test, pred_test)
print('테스트데이터:\n',confusion_test)

#정밀도 재현율 확인

from sklearn.metrics import classification_report 
cfreport_train = classification_report(y_train,pred_train)
print('분류예측리프토:\n',cfreport_train) #97,97


from sklearn.metrics import classification_report 
cfreport_test = classification_report(y_test,pred_test)
print('분류예측리프토:\n',cfreport_test) #97,97

#그리드 탐색
#hiden_layer_sizes은닉층 ,slover 옵티마이저, activation활성화함수 3가지 튜닝

param_grid ={'hiden_layer_sizes':[10,30,50,100],'slover':['sgd','adam'], 'activation':['tanh','relu']}

from sklearn.model_selection import GridSearchCV 
grid_search= GridSearchCV(MLPClassifier(),param_grid, cv=5)
grid_search.fit(X_scaled_train, y_train)

print('best parameter:{}'.format(grid_search.best_params_)) 
print('best score:{:4f}'.format(grid_search.best_score_))  
print('testset score:{:4f}'.format(grid_search.score(X_scaled_test, y_test))) 


#활성화tanh, 은닉청 100, 옵티마이저 adam 
#97%, 95%



#랜덤탐색

from scipy.stats import randint
param_distribs={'hiden_layer_sizes': randint(low=10, high=100),'slover':['sgd','adam'], 'activation':['tanh','relu']}

from sklearn.model_selection import RandomizedSearchCV 
random_search=RandomizedSearchCV(MLPClassifier(), param_distributions=param_distribs, n_iter=10, cv=5)
random_search.fit(X_scaled_train, y_train)


print('best parameter:{}'.format(random_search.best_params_)) 
print('best score:{:4f}'.format(random_search.best_score_))  
print('testset score:{:4f}'.format(random_search.score(X_scaled_test, y_test))) 

#활성화relu ,은닉층 51개 , 옵티마이저adam일때 좋은결과
#98%, 95%




##인공신경망 회귀

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


#인공신경망 회귀모델 적용
from sklearn.neural_network import MLPRegressor 
model=MLPRegressor()
model.fit(X_scaled_train, y_train)
pred_train=model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)  #-287%

pred_test=model.predict(X_scaled_test, y_test)
model.score(X_scaled_test, y_test)#-283%

#RSME확인
import numpy as np
from sklearn.metrics import mean_squared_error

MSE_train= mean_squared_error(y_train, pred_train)
MSE_test= mean_squared_error(y_test, pred_test)

print('훈련데이터',np.sqrt(MSE_train)) 
print('테스트데이터',np.sqrt(MSE_test)) 

#비이상적으로 큰값 전체적으로 잘 맞지 않다는것을 확인

##튜닝해주기!!
#그리드와 랜덤탐색은 하이퍼파라미터가 매우다양하여 최적의 조합을 찾는것이 어려움
#따라서 은닉층 3개를 두어 각각 64개의 노드를 구성하는 조금 깊은 모델 만들어보기!!


from sklearn.neural_network import MLPRegressor
model = MLPRegressor(hidden_layers_sizes =(64,64,64), activation='relu', random_state=1, max_iter=2000)
model.fit(X_scaled_train, y_train)
pred_train= model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)
#56%정확도

pred_test= model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)
#58%정확도


#RSME확인
import numpy as np
from sklearn.metrics import mean_squared_error

MSE_train= mean_squared_error(y_train, pred_train)
MSE_test= mean_squared_error(y_test, pred_test)

print('훈련데이터',np.sqrt(MSE_train)) 
print('테스트데이터',np.sqrt(MSE_test)) 

#62%, 61% 오차율 적음





















































