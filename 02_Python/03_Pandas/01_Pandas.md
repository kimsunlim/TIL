# Pandas

### <인덱싱, 데이터 조작, 인덱스 조작>

 



- loc():라벨값 기반의 2차원 인덱싱
- iloc():정수 기반의 2차원 인덱싱



1) import

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```



2)sample인덱싱&슬라이싱

```python
# df.loc(행 인덱싱값)
# df.loc(행 인덱싱값,열 인덱싱값)

sample_df = pd.DataFrame(np.arange(10,22).reshape(3,4),
                        index=['a','b','c'],
                        columns=['A','B','C','D'])
sample_df


sample_df.loc['a']    #인덱싱할 때는 대괄호!인덱스와 벨유로 나옴

type(sample_df.loc['a'].values) #type체크


#########

sample_df.loc['b':'c']   #슬라이싱으로 범위 지정 
```

![d](C:\Users\i\Desktop\d.PNG)

```python
#열인덱스
#sample_df.['A']
sample_df.A
```





3)라벨 없는경우

```python
sample_df2 = pd.DataFrame(np.arange(10,26).reshape(4,4),                
                        columns=['A','B','C','D'])
sample_df2

sample_df2.loc[1:2]
sample_df.loc['b':'c','A']
```

![s](C:\Users\i\Desktop\s.PNG)



4) iloc

```python
sample_df.iloc[0,1]
sample_df.iloc[:,1] #전체행
sample_df.iloc[0,-2:] # -는 뒤에서부터
sample_df.iloc[2,1:3]
```





- 데이터 갯수를 세어보자
- count



```python
s=pd.Series(range(10))  #시리즈 생성

s[5]=np.NaN
s[2]=np.NaN
s.count()
#값은 8

np.random.seed(2)
count_df=pd.DataFrame(np.random.randint(5, size=(4,4)),dtype=np.float64)


#결측값 쏙~!
count_df.iloc[1,0]=np.NaN
count_df.iloc[3,0]=np.NaN
count_df.iloc[2,3]=np.NaN
count_df.count
```



### 타이타닉 읽기

```python
import seaborn as sns
titanic = sns.load_dataset('titanic',engine='python')

titanic.info()
titanic.head()
titanic.count()  #각 열의 값을 볼수 있음
```



*열추가

```python
#새로운 열추가 age_0 일괄적으로 0할당
titanic['age_0']=0


#age의 각 값에 10을 곱한  age_by_10 컬럼 생성
titanic['age_by_10']= titanic['age']*10


#parch와 sibSp의 값과 1을 더한 family_no 컬럼 생성
titanic['family_no']= titanic['parch']+titanic['sibsp']
```





*데이터 삭제

```python
#agd_0열을 삭제한고자 한다면?
titanic_drop_df= titanic.drop('age_0',axis=1)  #axis 축!

titanic_drop_df=titanic.drop(['age_0','age_by_10','family_no'],axis=1,inplace=True)


#0,1,2 번째 행으 ㄹ삭제하여 원본 프레임에 반영하도록 한다면?
titanic.drop([0,1,2],axis=0,inplace=True)
```





*인덱스에 대한 슬라이싱 및 인덱싱



```python
#인덱스5개를 꺼내오고 싶다면?
titanic.index[:5].values

# 6인덱스꺼내오고 싶다면?
titanic.index[6]



#max,min,sum
print('max',series_fair.max())
print('min',series_fair.min())
print('sum',series_fair.sum())
print('DC 10%',series_fair *0.9)



#age>60이상인 정보만 추출하고 싶다면?

titanic_reset_index_df[titanic_reset_index_df['age']>60].head()


#age>60이상인 pclass,survied, who만 추출하고 싶다면?

titanic_reset_index_df[titanic_reset_index_df['age']>60][['pclass','survived','who']].head()

#나이 60보다 크고 선실 등급이 1등급이고 성별이 여자인 데이터를 추출한다면?

titanic_reset_index_df[titanic_reset_index_df['age']>60][['pclass'=1,'sex'= Female]].head()
```





```python
# 타이타닉호 승객의 평균나이를 구하라
print('타이타닉호 승객의 평균나이를 구하라 \n:',
     titanic_reset_index_df['age'].mean())


# 타이타닉호 승객중 여성승객의 평균나이를 구하라
female_index=titanic_reset_index_df['sex'] =='female'
print('타이타닉호 여성승객 평균나이를 구하라 \n:',
     titanic_reset_index_df.loc[ female_index,'age'].mean())

#타이타닉호 승객중 1등실 선실의 여성 승객의 평균나이를 구하라

pclass_index= titanic_reset_index_df['pclass'] ==1
wantde_index =female_index & pclass_index
print('타이타닉호 승객 중 1등 선실의 여성 승객의 평균나이를 구하라 \n:',
     titanic_reset_index_df.loc [wanted_index,'age'].mean())
```





## apply 변환

- 행이나 열 단위로 복잡한 데이터 가공이 필요한 경우
- **lambda식**
- apply 함수는 인자로 함수를 넘겨 받을수 있다.



```python
def get_square(a):
    return a**2

print("제곱근:",get_square(3))

#위 코드를 람다식으로 바꾼다면?
lambda_square=lambda a:a**2
print("제곱근:",lambda_square(3))


#각행의 column에 대해서 최대값-최소값을 구해 새로운column추가
#각 column안에서 최대값-최소값을 구해 출력
func =lambda  x :x.max()-x.min()

apply_df['row 최대-최소']=apply_df.apply(func,axis=1)



#embark_town의 문자열 개수를 별도의 컬럼인 embark_len 컬럼을 추가

titanic_reset_index_df['embark_len']=titanic_reset_index_df['embark_town'].apply(lambda x:len(str(x)))
titanic_reset_index_df[['embark_town','embark_len']].head(3)





## if ~else절을 활용하여 나이가 15세 이하면  child그렇지 않으면  adult 로 구분한는child_adult추가해라
titanic_reset_index_df['child_adult']=titanic_reset_index_df['age'].apply(lambda x : 'child' if x <15 else 'adult')
titanic_reset_index_df[['age','child_adult']].head(8)
```

