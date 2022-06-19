###### 작업형2 가이드라인

#########데이터 전처리

#0. 데이터 로딩
import pandas as pd
df= pd.read_csv('read')

#1. 결측치 제거 

##결측치 확인 
df.isnull(),sum( )


#결측치 중앙값과 특정 문자로 대체 
missing=['a','b']

for i in missing :
    df[i]=df[i].fillna(df[i].median())
    
df['c']=df['c'].fillna('Male')

#결측치 재확인
df.isnull().sum()



#2. 데이터라벨링
# 머신러닝이 잘 돌아가도록 문자형을 숫자형으로 변환 
#라벨인코딩

from sklearn.preprocessing import LabelEncoder
label=['a','b'] # 인코딩할 열 지정

df[label]=df[label].apply(LabelEncoder().fit_transform)


#3. 타입변환
#정수타입을 int타입으로 변환
#더미변수만들기 : 데이터가 옆으로 퍼지게하는것 > 성능 더 좋게함

df.dtypes #타입 확인 
category=['a','b']

for i in category:
    df[i]=df[i].astype('category')
    
df=pd.get_dummies(df) #df를 더미변수화 시킴



#4. 파생변수 생성 
# 변수가 다양해야 모델성능이 좋아짐 

#데이터 구간화 

df['c']=pd.qcut(df['a'],5,label=False) ##5구간으로 나눠 파생변수 생성

df['c'].value_counts()



#5. 스케일링
#학습시킬 때 숫자 단위가 다양하면 이상치 발생
#특정값이 영향을 많이 받게됨

#민맥스 : 0~1 사이 값으로 변환

from sklearn.prepreocessing import MinMaxScaler
s=['a']
scaler=MinMaxScaler()
scaler.fit(df[s])
df[s]=scaler.transform(df[s])


#6. 데이터셋 분할
#훈련데이터와 테스트 데이터 

from sklearn.model_selections import train_test_split 

X_train, X_test, y_train, y_test =train_test_split(df.iloc[:,1:],df['species'],
                                                   test_size=0.2, stratify=df['species'], randomstate=1)

X_train.shape() #잘 분리 되었는지 확인





########## 모델학습



#7. 모형학습 

##앙상블사용

#1). 랜덤포레스트

from sklearn.ensemble import RandomForestClassifier 
model1=RandomForestClassifier()

model1.fit(X_train, y_train) #모델학습
pred_test1=model1.predict(X_test) #테스트데이터 예측

#2). AdaboostClassifier

from sklearn.ensemble import AdaBoostClassifier

model2=AdaBoostClassifier()
model2.fit(X_train, y_train)
pred_test2=model2.predict(X_test)


#8. 앙상블 보팅> 랜포와 에이다 투표를 해서 선택

from sklearn.ensemble import VotingClassifier 
clf=VotingClassifier(estimators=[('rf',model1),('ad',model2)], voting='hard')
clf.fit(X_train, y_train)
pred_test3=clf.predict(X_test)


#9. 모형평가 


from sklearn.metrics import accuracy_score

print('랜포 정확도', accuracy_score(y_test,pred_test1))
print('에이다 정확도', accuracy_score(y_test,pred_test2))
print('보팅 정확도', accuracy_score(y_test,pred_test3))

###100인거 확인 


#10. 하이퍼파라미터 튜닝
##빅분기에서 여기까지는 안해도 됨

from sklearn.model_selection import GridSearchCV
parameters={'n_estimators':[50,100], 'max_depth':[4,6]}

model4=RandomForestClassifier()
clf=GridSearchCV (esimator=model4, param_grid=parameters, cv=3)
clf.fit(X_train, y_train)

print('최적 파라미터', clf.fit.best_params_)



#11. 예측값 저장
#랜포랑 보팅이 성능 제일 좋은 상황

#열이름 id > y_test index
#예측된 값의 열이름 pred >pred_test3 으로 가져오기
#데이터프레임 생성

#index=False 꼭하기!!! 제출 형식과 맞아야함 안하면 떨어짐 !!매우 중요~!~!

pd.DataFrame({'id':y_test.index, 'pred':pred_test3}).to_csv('123.csv', indes=False)




#제출 한 다음 다시 불러와야함 //확인을 위해
check= pd.read_csv('123.csv')
check.head()



##랜포와 에이다 부스트가 가장 베이스라인 모델
#랜포는 병렬로 약한 학습기로 학습
#에이다 부스트는 부스팅 > 순차적으로 학습 > 강한 분류기로 성능 냄 





