# Pandas [03]



1. **그룹 분석 및 피봇**

**1)**

- Series Grouping



```python
df = pd.DataFrame({ "학과" : ["컴퓨터","체육교육과","컴퓨터","체육교육과","컴퓨터"],
                    "학년" : [1, 2, 3, 2, 3],
                    "이름" : ["홍길동","김연아","최길동","아이유","신사임당"],
                    "학점" : [1.5, 4.4, 3.7, 4.5, 3.8]})
```



![캡처](C:\Users\i\Desktop\캡처.PNG)

- **학과를 기준으로 Grouping**
- **groupby()**



```python
dept_serirs=df['학과'].groupby(df['학과'])
```



- get_group

```python
dept_serires.get_group('컴퓨터')  #컴퓨터가 시리즈로 리턴 
```



-  size  각 그룹의 사이즈를 확인!

```python
dept_serires.size()

#체육교육학과 2
#컴퓨터 3
#으로 출력~!
```



- mean ,sum

```python
dept=df.groupby(df['학과'])
dept


dept.mean()
dept.sum()


df.groupby(['학과','학년']).mean()
```





- load_dataset  : 데이터 로드

```python
iris=sns.load_dataset('iris')
iris

iris.describe()  #표준편차,평균,섬등 나타냄
```

![ff](C:\Users\i\Desktop\ff.PNG)



- 비율구하기
- 각 종별로 가장 큰 값과 가장 작은 값의 비율을 구한다면?

```python
#함수 생성
def get_ratio(x):
    return x.max()/x.min()

#적용
iris.groupby(iris.species).agg(get_ratio)
#가로로 정렬
iris.groupby(iris.species).describe().T
```



- #붓꽃 종별로 가장 큰 꽃잎길이가 큰 3개의 데이터를 뽑아내는 함수정의

```python
#함수생성
def max3_petal_length_func(df):
    return df.sort_values (by='petal_length',ascending=False)[:3]

iris.sort_values(by='petal_length',ascending=False)[:3]

#적용
iris.groupby(iris.species).apply(max3_petal_length_func)
```





**2)**

- transform :데이터 프레임 자체를 변화 시키는 함수
- 원본 프레임과 크기가 같다
- 각 붓꽃 꽃잎길이가 해당 종 내에서 대/중/소 어느것에 해당되는지에 대한 프레임을 만들고 싶다면?
- cut():동일 길이로 나누어서 범주를 만들어서 그룹에 대한 통계량
- qcut():동일 갯수로 나누어서 범주를 만들어서 그룹에 대한 통계량



```python
 
#그룹
iris.groupby(iris.species)
    
iris.groupby(iris.species).petal_length.size()
```



=대중소

```python
def cat3_petal_length(s):
    return pd.qcut(s,3,labels=['소','중','대']).astype(str)

iris['category']=iris.groupby(iris.species).petal_length.transform(cat3_petal_length)
iris.head()
```



- 붓꽃 데이터에서 붓꽃종별로 꽃잎길이, 꽃잎폭등의 평균을 구하라

```python
iris.groupby(iris.species).agg(np.mean).loc[: ,['sepal_length','sepal_width']]  
#agg는 하나 이상의 집계함수 사용 가능,apply는 하나만 사용가능
```





2. **pivot**
   - 데이터 프레임에서 두개의 열을 이용하여 행/열 인덱스 reshape된 테이블을 의미한다
   - 새로운 테이블에서 새로운 기준 집계
   - pivlot(index, columns,values)
   - pivlot_table(data,values,index,columns,aggfunx='mean')

1) 타이타닉 sample

```python
titanic= sns.load_dataset('titanic')
titanic.head()

titanic_df01 =pd.DataFrame(titanic,columns=['sex','pclass'])
titanic_df01.head()
```



- 성별과 객실등급에 다른 승객 수 집계

```python
titanic_df01=titanic.groupby(['sex','pclass']).size().reset_index(name='cnt') 
#인덱스 재조정
titanic_df01
```



- 성별과 생존여부에 따른 승객 수 집계한다면?

```python
titanic_df02=titanic.groupby(['sex','survived']).size().reset_index(name='cnt')   #인덱스 재조정
titanic_df02
```



- 성별과 객실등급에 따른 승객 수 집계
  =pivot_table

```python

titanic['cnt'] =1

titanic.pivot_table('cnt','sex','pclass',aggfunc=np.sum)
titanic.pivot_table('cnt','sex','survived',aggfunc=np.sum)

```





--------

2) 도시 sample



```python
data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}
columns = ["도시", "연도", "인구", "지역"]
pivot_sample_df = pd.DataFrame(data, columns=columns)
pivot_sample_df

```

![fsafs](C:\Users\i\Desktop\fsafs.PNG)





- pivot_table option
- data: 데이터 프레임
- values: 분석할 열
- index
- columns
- aggfunc: 집계함수
- fill_value: NaN대체값
- margins:분석결과를 오른쪽과 아래에 붙일지 여부, 집계함수 추출
- margins_name:마진 열의 이름



```python
pivot_sample_df.pivot_table('인구','도시','연도',margins=True,margins_name='분석결과')

tips =sns.load_dataset('tips')
tips.head()

```



- 식사 대급 대비 팁의 비율이 어떤경우에 가장 높은지 찾는다면?

```python
tips['tip/pct']=tips['tip']/tips['total_bill']
tips.head()
tips.describe()
tips.groupby('sex').count()
```



- 성별과 흡연유무로 나누어서 데이터 갯수를 세어본다면?

```python
tips.groupby(['sex','smoker']).count()
tips.pivot_table('tip/pct','sex','smoker',aggfunc='count',margins=True)
```





- 성별과 흡연여부에 따른 평균 팀 비율 살펴본다면?

```python
tips.groupby (['sex','smoker'])[['tip/pct']].mean()
```







3) 타이타닉 sample

- 1.qcut 명령으로 세 개의 나이 그룹을 만든다. 0~19 : A 20~59 : B 60 ~ : C

```python
titanic['age_cut']=pd.qcut(titanic['age'],3,labels=['A','B','C'])
titanic.head()
```

  

- 2.성별, 선실, 나이 그룹에 의한 생존율을 데이터프레임으로 계산한다. 행에는 성별 및 나이 그룹에 대한 다중 인덱스를 사용하고 열에는 선실 인덱스를 사용한다. 생존률은 해당 그룹의 생존 인원수를 전체 인원수로 나눈 값이다.

```python
count_df=titanic.pivot_table('survived',['sex','age_cut'],'pclass',
                             aggfunc='count',
                             margins=True,
                             margins_name='sur_ratio')
all_count =count_df.loc['sur_ratio','sur_ratio'][0]
survival_rate_df =count_df /all_count

display(count_df)
display(survival_rate_df)
                            
```



- 3. 성별 및 선실에 의한 생존율을 피봇 데이터 형태로 만든다.



```python
count_df=titanic.pivot_table('survived','sex','pclass',
                             aggfunc='sum',
                             margins=True,
                             margins_name='sur_ratio')
all_count =titanic.shape[0]
survival_rate_df=count_df /all_count
display(survival_rate_df)
```

