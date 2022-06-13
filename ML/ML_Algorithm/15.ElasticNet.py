##엘라스틱넷 
# Elasticnet 
#릿지와 라쏘 절충한 모델
#혼합비율 r을 사요해서 조절 


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

## 엘라스틱넷 모델 적용

from skelarn.linear_model import ElasticNet 
model=ElasticNet()
model.fit(X_scaled_train, y_train)
pred_train=model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)

pred_test=model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)



##RMSE

import numpy as np 
from sklearn.metrics import mean_squared_error 

MSE_train = mean_squared_error(y_train, pred_train)
MSE_test = mean_squared_error(y_test, pred_test)
print(np.sqrt(MSE_train))
print(np.sqrt(MSE_test))
#93,93

##  grid search

param_grid={'alpha':[0.0,1e-6,1e-5,1e-4,1e-3,1e-2,0.1,0.5,1.0,2.0,3.0]}

from sklearn.model_selection import GridSearchCV
grid_search= GridSearchCV(ElasticNet(), param_grid, cv=5)
grid_search.fit(X_scaled_train, y_train)

            
print('best parameter:{}'.format(grid_search.best_params_)) 
print('best score:{:4f}'.format(grid_search.best_score_))  
print('testset score:{:4f}'.format(grid_search.score(X_scaled_test, y_test)))


##랜덤서치


from scipy.stats import randint 

param_distribs ={'alpha': randint(low=0.00001, high=10)}
             
                                 
from sklearn.model_selection import RandomizedSearchCV 
random_search=RandomizedSearchCV(ElasticNet(), param_distributions=param_distribs, n_iter=100, cv=5)
random_search.fit(X_scaled_train, y_train)
            
print('best parameter:{}'.format(random_search.best_params_)) 
print('best score:{:4f}'.format(random_search.best_score_))  
print('testset score:{:4f}'.format(random_search.score(X_scaled_test, y_test))) 