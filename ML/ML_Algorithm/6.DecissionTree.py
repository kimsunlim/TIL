
##의사결정나무 decision tree

# 집단을 몇개의 소집단으로 분류 하거나 특정값을 예측
# root node는 뿌리마디 이며 레이블(y)임
# intermediate node 중간 노드
# terminal node 끝마디

#직관적으로 도식화하여 어떻게 분류되는지 알수 있다는 장점
#단계가 많아지면 불안정적 이어서 머신러닝 알고리즘으로는 많이 사용안함





##의사결정나무 분류

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


#의사결정나무 분류모델 적용

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_scaled_train, y_train)
pred_train=model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)

#정확도 100


pred_test= model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)

#정확도 95%


#오차행렬 확인

from sklearn.metrics import confusion_matrix
confusion_train = confusion_matrix (y_train, pred_train)
print('훈련데이터:\n',confusion_train)



confusion_test = confusion_matrix (y_test, pred_test)
print('훈련데이터:\n',confusion_test)

#분류예측리포트 확인

from sklearn.metrics import classification_report 
cfreport_train = classification_report(y_train,pred_train)
print('분류예측리프토:\n',cfreport_train) 


from sklearn.metrics import classification_report 
cfreport_test = classification_report(y_test,pred_test)
print('분류예측리프토:\n',cfreport_test) 


#모델튜닝
##그리드 탐색


param_grid={'max_depth':range(2,20,2),'min_samples_leaf': range(1,50,2)}
from sklearn.model_selection import GridSearchCV 
grid_search=GridSearchCV(DecisionTreeClassifier(),param_grid, cv=5)

grid_search.fit(X_scaled_train, y_train)


print('best parameter:{}'.format(grid_search.best_params_)) 
print('best score:{:4f}'.format(grid_search.best_score_))  
print('testset score:{:4f}'.format(grid_search.score(X_scaled_test, y_test))) 



#max depth 는 6, minsamplesleaf는 1일때 최적
#96, 94 정확도 확인

##랜덤탐색
 
from scipy.stats import randint 
param_distribs={'max_depth': randint(low=1, high=20),
                'min_samples_leaf':randint(low=1, high=50)}

from sklearn.model_selection import RandomizedSearchCV 
random_search=RandomizedSearchCV(DecisionTreeClassifier(), param_distribution=param_distribs, n_iter=20, cv=5)
random_search.fit(X_scaled_train, y_train)



            
print('best parameter:{}'.format(random_search.best_params_)) 
print('best score:{:4f}'.format(random_search.best_score_))  
print('testset score:{:4f}'.format(random_search.score(X_scaled_test, y_test))) 


#max depth 는 13, minsamplesleaf는 2일때 최적
#95, 94 정확도 확인


##과적합 되는 경향이 있어서 100%가 나옴 하이퍼파라미터 논리적으로 설정하기 어려움 
#그래도 초기모델로는 사용 괜춚




##의사결정나무 회귀



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



#의사결정나무 회귀 모델 적용

from sklearn.tree import DecisionTreeRegressor 

model=DecisionTreeRegressor()
model.fit(X_scaled_train, y_train)
pred_train=model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)

#정확도 100


pred_test= model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)

#정확도 21.7


##RSME확인

import numpy as np
from sklearn.metrics import mean_squared_error

#오차 훈련데이터
MSE_train=mean_squared_error(y_train,pred_train) #0
MSE_test=mean_squared_error(y_test,pred_test)  #84

print('훈련데이터',np.sqrt(MSE_train)) 
print('테스트데이터',np.sqrt(MSE_test)) 

##훈련데이터에 과대적합







#모델 튜닝

#그리드탐색

param_grid ={'max_depth':range(2,20,2),'min_samples_leaf':range(1,50,2)}

              
      
                                                    
from sklearn.model_selection import GridSearchCV 
grid_search= GridSearchCV(DecisionTreeRegressor(),param_grid, cv=5)
grid_search.fit(X_scaled_train, y_train)

print('best parameter:{}'.format(grid_search.best_params_)) 
print('best score:{:4f}'.format(grid_search.best_score_))  
print('testset score:{:4f}'.format(grid_search.score(X_scaled_test, y_test))) 



#max depth 는 8, minsamplesleaf는 49일때 최적
#55, 57 정확도





#랜덤탐색 

from scipy.stats import randint 

param_distribs ={'max_depth':randint(low=1, high=20),'min_samples_leaf':randint(low=1, high=50)}
                 
                 
from sklearn.model_selection import RandomizedSearchCV 
random_search=RandomizedSearchCV(DecisionTreeRegressor(), param_distributions=param_distribs, n_iter=20, cv=5)
random_search.fit(X_scaled_train, y_train)
            
print('best parameter:{}'.format(random_search.best_params_)) 
print('best score:{:4f}'.format(random_search.best_score_))  
print('testset score:{:4f}'.format(random_search.score(X_scaled_test, y_test))) 



#max depth 는 9, minsamplesleaf는 48일때 최적
#55, 57 정확도


##회귀모델도 과대적합 경향보임


