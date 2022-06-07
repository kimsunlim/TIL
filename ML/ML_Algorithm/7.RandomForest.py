
#랜덤 포레스트 RandomForest
#여러 결정 트리를 앙상블 하는것


###############분류

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

#랜덤포레스트 분류 모델 적용

from sklearn.enesemble import RandomForestClassifier 
model= RandomForestClassifier()

model.fit(X_scaled_train, y_train)
pred_train = model. predict(X_scaled_train)
model.score(X_scaled_train, y_train)


pred_test = model. predict(X_scaled_test)
model.score(X_scaled_test, y_test)


#100% >>과대적합 나옴

#오차행렬로 확인

from sklearn.metrics import confusion_matrix 
confusion_train= confusion_matrix(y_train, pred_train)
print(confusion_train)


confusion_test= confusion_matrix(y_test, pred_test)
print(confusion_test)

##100%

#분류레포트
from sklearn.metrics import classification_report
cfreport_test= classification_report(y_test, pred_test)
print(cfreport_test)



## 모델튜닝
#Grid search

param_grid={'n_estimators': range(100,1000,100),
            'max_features':['auto','sqrt','log2']}


from sklearn.model_selection import GridSearchCV
grid_search =GridSearchCV(RandomForestClassifier(), param_grid, cv= 5)
grid_search.fit(X_scaled_train, y_train)


print('best parameter:{}'.format(grid_search.best_params_)) 
print('best score:{:4f}'.format(grid_search.best_score_))  
print('testset score:{:4f}'.format(grid_search.score(X_scaled_test, y_test))) 




# n_estimators 300, max_features auto 일떄 최적화
# 97.5 96.5 정확도


#randomsearch

from scipy.stats import randint

param_distibs ={'n_estimators': randint (low=100,high=1000),
            'max_features':['auto','sqrt','log2']}



from sklearn.model_selection import RandomizedSearchCV 
random_search=RandomizedSearchCV(RandomForestClassifier(), param_distribution=param_distibs, n_iter=20, cv=5)
random_search.fit(X_scaled_train, y_train)



            
print('best parameter:{}'.format(random_search.best_params_)) 
print('best score:{:4f}'.format(random_search.best_score_))  
print('testset score:{:4f}'.format(random_search.score(X_scaled_test, y_test))) 


# n_estimators 672, max_features auto 일떄 최적화
# 97.5 96.5 정확도






################회귀

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



##랜덤포레스트 회귀 모델

from sklearn.ensemble import RandomForestRegressor 
model=RandomForestRegressor()

model.fit(X_scaled_train, y_train)
pred_trian =model. predict (X_scaled_train) 
model.score(X_scaled_train,y_train)

#93%

pred_test =model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)

#58%



#Rmse

import numpy as np

from sklearn.metrics import mean_squared_error 
MSE_train= mean_squared_error(y_train, pred_train)
MSE_test= mean_squared_error(y_test, pred_test) 


print(np.sqrt(MSE_train))
print(np.sqrt(MSE_test))




##모델튜닝
#Grid search

param_grid ={'n_estimators': range(100, 500, 100 ),
             'max_features':['auto','sqrt','log2']}

from sklearn. model_selection import GridSearchCV 

grid_search =GridSearchCV (RandomForestRegressor(), param_grid, n_iter=20 , cv=5 )
grid_search. fit(X_scaled_train, y_train)



print('best parameter:{}'.format(grid_search.best_params_)) 
print('best score:{:4f}'.format(grid_search.best_score_))  
print('testset score:{:4f}'.format(grid_search.score(X_scaled_test, y_test))) 


# n_estimators 400, max_features log2 일떄 최적화
# 56%, 59% 


#random search

param_distribs= {'n_estimators': randint (low=100, high= 500 ),
             'max_features':['auto','sqrt','log2']}


from sklearn.model_selection import RandomizedSearchCV 

random_search = RandomizedSearchCV(RandomForestRegressor(), param_distributions= param_distribs, n_iter=20, cv=5)
random_search.fit(X_scaled_train, y_train)


print('best parameter:{}'.format(random_search.best_params_)) 
print('best score:{:4f}'.format(random_search.best_score_))  
print('testset score:{:4f}'.format(random_search.score(X_scaled_test, y_test))) 

# n_estimators 358,  max_features sqrt 일떄 최적화
# 56%, 57% 






# 디폴트 모델에서 과대적합되는 경향이 있음
# 적절한 모델수와 특성치를 탐색한 결과 좋은 결과를 보임

#게별 알고리즘보다 더 좋은 성




















