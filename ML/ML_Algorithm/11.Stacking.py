
##Ensemble Stacking
#스태킹

#여러 학습기에서 예측한 예측값으로 다시 학습 데이터를 만들어 일반화 하는것


##분류
#랜덤포레스트, 서포트 벡터머신 사용 
#최종모델 로지스틱
#보팅과 비슷
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

###모델 적용

from sklearn.ensemble import RandomForestClassifier 
from sklearn.svm import SVC 
from sklearn.linear_model import LogisticRegression 
from sklearn.ensemble import StackingClassifier 

estimators=[('rf', RandomForestClassifier(n_estimators=10, random_state=42)), ('svr', SVC(random_state=42))]
model=StackingClassifier(estimators=estimators, final_estimaors= LogisticRegression())
model.fit(X_scaled_train, y_train)
pred_train = model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)


# 98% 

##혼동행렬
from sklearn.metrics import confusion_matrix 
confusion_train =confusion_matrix(y_train, pred_train)
print(confusion_train)


##분류리포트

from sklearn.metrics import classification_report
cfreport_train = classification_report(y_train, pred_train)



##스태킹 앙상블은 모델을 어떻게 쌓는가에 따라서 결과가 달라진다. 
#순서를 변경하거나 다른 알고리즘을 쓰면 개선 될수도 있음




##회귀
#선형회귀와 KNN사용
#최종모델은 랜포




from sklearn.ensemble import LinearRegression 
from sklearn.neighbors import KNeighboreRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.ensemble import StackingRegressor


estimators=[('lr', LinearRegression()), ('knn', KNeighborsRegressor())]
model=StackingRegressor(estimators=estimators, final_estimator=RandomForestRegressor(n_estimators=10, random_state=42))

model.fit(X_scaled_train, y_train)
pred_train=model.fit(X_scaled_train)
model.score(X_scaled_train, y_train)

#54%


pred_test=model.fit(X_scaled_test)
model.score(X_scaled_test, y_test)

#47% 



import numpy as np

from sklearn.metrics import mean_squared_error

MSE_train= mean_squared_error(y_train, pred_train)
MSE_test= mean_squared_error(y_test, pred_test)

print(np.sqrt(MSE_train))





















