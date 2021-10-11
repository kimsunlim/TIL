###  웹크롤링



#### 비정형 데이터

> web scraping(web content- BeautifulSoup)

:  웹사이트에서 원하는 부분에 위치한 정보를 추출하는 기술(정적 페이지)

> web crawling (Selenium)

:자동화 봇

:링크를 따라 돌면서 연결된 페이지를 가져오는 기술



####  1. 기본적으로 import 해주는것

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
```

```python
try:
    html = urlopen('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')
except HTTPError as he:
    print('http error')
except URLError as ue:
    print('url error')
else:
    soup = BeautifulSoup(html.read(),'html.parser')
```





#### 2.스크래핑(Beautifulsoup)

``` python
#import해주기
import requests 
from bs4 import BeautifulSoup


#웹페이지 가져오기

webpage=requests.get('https://www.daangn.com/hot_articles')
#webpage.text
soup = BeautifulSoup(webpage.content,'html.parser')
```



####  3.태그탐색하기

print(soup.p) ->p태그 가져오는거

print(soup.h1) ->h1태그 가져오는거



```python
for child in soup.h1.children:    #h1안에 자식찾기
    print(child)
    
    
for d in soup.div.children:
    print(d)
    
```



#### 4. find_all( ):원하는 부분 모두 가져오기

- print(soup.find_all('h2'))

- soup.find_all(re.compile('h[1-9]'))

- soup.find_all(['h1','p'])
- soup.find_all(attrs={'class':'card-title'})
- soup.select('.card-title')
- soup.select('#hot-articles-navigation')

```python
for idx in range(0,10):
    print(soup.select('.card-title')[idx].get_text())
    
```



#### 5. 데이터를 가져오는 방법

1)import 하고, 링크 넣기 (기본적 import)

2)soup로 데이터확인

3) id="seven-day-forecast"추출

```python
sevenDays=soup.find(id="seven-day-forecast")
sevenDays
```

4)

```python
forecast=sevenDays.find_all(class_ ='tombstone-container')
period=forecast[0].find(class_ ='period-name').get_text()

```



5)

```python
short_desc =forecast[0].find(class_ ='short-desc').get_text()
short_desc
```





6)이미지 추출

```python
img=forecast[0],find('img')
img_src=img['src']
img_src
```



7)

```python 
sevenDays=soup.select("#seven-day-forecast")
```



#### 6 필요한 기상 정보 전체 가져오기

1)기상정보 9개 추출

```python 
sevenDays=soup.find(id ='seven-day-forecast')
periods=sevenDays.select('.tombstone-container .period-name')
periods
```

2) 날짜만 추출

```python
periods_text=[text.get_text() for text in periods]
periods_text
```

3)

```python
descs = sevenDays.select('.tombstone-container .short-desc')
descs

desc_text=[text.get_text()for text in descs]
desc_text

temp_text=[text.get_text() for text in sevenDays.select('.tombstone-container .temp')]
temp_text
```



4)필요 변수 print

```python
print(len(periods_text))
print(len(desc_text))
print(len(temp_text))
```



5)판다스 import

**import pandas as pd**



6) 판다스로 셀표현

```python
forecast_df =pd.DataFrame({
    'period':periods_text,
    'desc'  :desc_text,
    'temp': temp_text
    })

forecast_df
```



7 )csv로 저장

**forecast_df.to_csv('forecast_df.csv',mode='w',encoding='utf-8')**
**print('success')**