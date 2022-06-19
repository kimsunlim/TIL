import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split

df=sns.load_datas('titanic')
print(df.head())
X_train, X_test,y_train, y_test=train_test_split(df,df['survived'], test_size=0.2, random_strate=42, stratify=df['survived'])
X_train =X_train.drop (['alive','survived'],axis=1)
X_test =X_test.drop (['alive','survived'],axis=1)


#1. 결측치 제거 

#결측치확인
print(X_train.isna().sum())

#ages > 평균값
#문자형은 분포도를 보고 가장 많은값 넣을 것
print(X_train['deck'].value_counts())


#결측치 제거
missing=['age']
for i in missing:
    X_train[i]=X_train[i].fillna(X_train[i].mean())
    X_test[i]=X_test[i].fillna(X_test[i].mean())
    
X_train['deck']=X_train['deck'].fillna('c')
X_test['deck']=X_test['deck'].fillna('c')

X_train['embarked']=X_train['embarked'].fillna('s')
X_test['embarked']=X_test['embarked'].fillna('s')


print(X_train.isna().isnull())



#2. 라벨 인코딩
from sklearn.preprocessing import LabelEncoder

#문자열들 라벨로 할건데 확인
label= ['sex','embarked','class','who','adult_male','deck']
X_train[label]=X_train[label].apply(LabelEncoder().fit_transform)
X_test[label]=X_test[label].apply(LabelEncoder().fit_transform)



#3. 데이터타입변환, 더미
 
print(X_train.dtypes)

dtype=['pclass','sex','class'] #리스트로 묶어 카테고리화
for i in X_train[dtype]: 
    X_train[i]=X_train[i].astype('category')
    
for i in X_test[dtype]: 
    X_test[i]=X_test[i].astype('category')
    
    
X_train=pd.get_dummies(X_train)
X_test=pd.get_dummies(X_test)


#4. 파생변수 
#연속변수 나이 
#age를 5구간으로 나눈 age_qcut 파생 변수 생성 
X_train['age_qcut']=pd.qcut(X_train['age'],5,labels=False)
X_test['age_qcut']=pd.qcut(X_test['age'],5,labels=False)


#5. 스케일 
#age,fare 연속형이라 맞추기
from sklearn.preprocessing import MinMaxScaler

scaler=['age','fare']
min=MinMaxScaler()
min.fit(X_train[scaler])

X_train[scaler]=min.transfom(X_train[scaler])
X_test[scaler]=min.transfom(X_test[scaler])


#6. 데이터 분리 
#학습이 잘되는지 검증용 데이터셋 만드는것
X_train, X_valid, y_train, y_valid =train_test_split(X_train, y_train,test_size=0.2, random_state=42, stratify=y_train)
    
print(X_train.shape()) #잘 분리 됬는지 확인가능


#7. 모형학습 
#랜포, 로지스틱 , 보팅

from sklearn.linear_model import LogisticRegression 
model1=LogisticRegression()
model1.fit(X_train, y_train)
pred1=pd.DataFrame(model1.predict_proba(X_valid))


#확률 예측해야할때는 predict_proba


from sklearn.ensemble import RandomForestClassifier
model2=RandomForestClassifier()
model2.fit(X_train, y_train)
pred2=pd.DataFrame(model2.predict_proba(X_valid))
     



#8. 앙상블 보팅 
#확률구하는거라 soft 사용
from sklearn.ensembel import VotingClassifier
model3=VotingClassifier(estimators=[('Logistic',model1),('random',model2)], voting='soft')
model3.fit(X_train,y_train)
pred3=pd.DdataFrame(model3.predict_proba(X_valid))


#9.모형 평가
#roc-auc 

from sklearn.metrics import roc_auc_score
print('로지스틱', roc_auc_score(y_valid,pred1.iloc[:,1])) #전체행의 첫번째열
print('랜포', roc_auc_score(y_valid,pred2.iloc[:,1])) 
print('보팅', roc_auc_score(y_valid,pred3.iloc[:,1])) 


#10.하이퍼파라미터 튜닝
from sklearn.model_selection import GridSearchCV
parameters= {'n_estimators':[50,100], 'max_depth':[4,6]}
model5=RandomForestClassifier()
clf=GridSearchCV(estimator=model5, param_grid=parameters,cv=3)
clf.fit(X_train, y_train)

print('최적 파라미터',clf.best_params_)

#11. 파일저장 

result=pd.DataFrame(model3.predict_proba(X_test))
result=result.iloc[:,1]

pd.DataFrame({'id':X_test.index,'result':result}).to_csv('0003.csv',index=False)

