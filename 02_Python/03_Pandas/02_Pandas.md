# pandas [02]



#### 1. filna :NaN 값을 원하는 값으로 변경 가능



```python
#샘플을 만들어보쟝
sample_df =pd.DataFrame({
    'A':[1,3,4,3,4],
    'B':[2,3,1,2,3],
    'C':[1,5,2,4,4]
})
sample_df

# 결측값 넣기

sample_df.iloc[2,2]=np.nan

#결측값에 0.0 넣음
sample_df.apply(pd.value_counts).fillna(0.0)
```



#### 2. astype:자료형을 바꾸는 기능

```python
sample_df.apply(pd.value_counts).fillna(0).astype(int)
```





#### 3.데이터 프레임 인덱스 조작하는 법

- set_index: 기존 행 인덱스를 제거하고 데이터 열 중 하나를 인덱스로 설정
- reset_index: 기존 행 인덱스를 제거하고 인덱스를 데이터 열 추가



```python
np.random.seed(100)
index_df=pd.DataFrame(np.vstack([list('ABCDE'),
                                np.round(np.random.rand(3,5),2)]).T,
                     columns=['col01','col02','col03','col04'])
index_df

#set_index: 
index_df2=index_df.set_index('col01')

#reset_index:
index_df2.reset_index()
```



#### 4.Data Frame merge



1)sample

```python
data1 ={
    '학번':[1,2,3,4],
    '이름':['섭섭해','김한준','김선림','최호진'],
    '학력':[2,4,1,3]
}



data2 ={
    '학번':[4,3,2,1],
    '학과':['CS','MATH','MATH','CS'],
    '학점':[2.4,4.5,3.4,3.2]
}

stu_df = pd.DataFrame(data1)
major_df = pd.DataFrame(data2)
display(stu_df)
display(major_df)

```



2)merge하기

```python
pd.merge(stu_df,major_df, on='학번',how='inner')
pd.merge(stu_df,major_df, on='학번',how='left')
pd.merge(stu_df,major_df, on='학번',how='right')
```



3)컬럼 인덱스가 아닌, 인덱스를 기준으로 병합한다면?

```python
pop_df02 =pd.DataFrame(np.arange(12).reshape((6,2)),
    index = [['busan','busan','seoul','seoul','seoul','seoul'],
             [2010,2005,2020,2018,2015,2020]],
    columns= ['col01','col02']
)
pop_df02
```

+merge

```python
pd.merge(pop_df01,pop_df02,left_on=['city','year'],right_index=True)
```



4)다중 인덱스가 아닌 단일 인덱스를 이용하는 방법



```python
data1 = { "이름" : ["이지안","박동훈","이순신","강감찬"],
          "학년" : [2,4,1,3]}

data2 = { "학과" : ["CS","MATH","MATH","CS"],
          "학점" : [3.4,2.9,4.5,1.2]}
```

```python
df01 = pd.DataFrame(data1, index=[1,2,3,4])
df02 = pd.DataFrame(data2, index=[1,2,4,5])


display(df01)
display(df02)
```

+merge

```python
merge_df=pd.merge(df01,df02,right_index=True,left_index=True)


#join
df01.join(df02, how='inner')
```

