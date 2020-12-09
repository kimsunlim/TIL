

##  야구 웹 크롤링



1)import하기

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')
except HTTPError as he:
    print('http error')
except URLError as ue:
    print('url error')
else:
    soup = BeautifulSoup(html.read(),'html.parser')
    
    soup
```

2)find하기

```python
table=soup.find('table',{'class':'table_develop3'})   #속성값에 따라 class, id지정
table
```

3)for 구문

```python
for tr in table.find_all('tr'):
    tds=list(tr.find_all('td'))
    for td in tds:
        print(td)
        
        
point_list=[]
temp_list=[]
humidity_list=[]
for tr in table.find_all('tr'):
    tds=list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):
            point=td.find('a').text
            point_list.append(point)
            temp=tds[5].text
            temp_list.append(temp)
            humidity=tds[9].text
            humidity_list.append(humidity)
```

4)

```python
import pandas as pd
weather_df =pd.DataFrame({
    'point':point_list,
    'temp'  :temp_list,
    'humidity': humidity_list
    
})



weather_df.to_csv('weather_df.csv',mode='w',encoding='utf-8')
print('success')

```









**++**



```python
with open('2020KBObatter.csv','w',encoding="utf-8")as file:
    file.write('player, bat_average,hit,homerun,RBI\n')
    
for idx in data:
    file.write('{},{},{},{},{}\n'.format(idx[0],idx[1],idx[2],idx[3],idx[4]))
    
    
   
#전처리를 하고 시각화
    
    

    
%matplotlib inline

import pandas as pd

import matplotlib as mpl

import matplotlib.pyplot as plt


df= pd.read_csv('./2020KB0batter.csv',indx_col='player',encoding='utf-8')

df


df .plot.bar()

```

