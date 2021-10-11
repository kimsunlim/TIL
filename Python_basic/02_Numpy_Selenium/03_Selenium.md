## Selenium

브라우저 동작을 자동화 해주는 프로그램

브라우저 동작시킨다는 의미는

javascript가 동작하면서 비동기적으로 서버로부터 콘텐츠를 가져오는 의미

콘텐츠를 가져오는 의미

-json 형식으로!



```python
condainstall -c conda -forge selenium
```

**or**

```python
pip install selenium
```



#### Selenium 시작하기

```python
from selenium import webdriver


path = './driver/chromedriver.exe'
driver = webdriver.Chrome(path)
driver


driver.get('https://www.google.com')
```



#### - json형식의 파일 크롤링

- import하기

```python
import json,re
from urllib.request import urlopen
from html import unescape
```

- 웹페이지 읽어오기

```python
request =urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
encoding=request.info().get_content_charset('utf-8')
html=request.read().decode(encoding)
html
```

- json.dump():데이터를 json형태로 인코딩(문자열)
- json.dimp():데이터를 json형태로 인코딩하여 파일에 출력(파일)
- ensure_ascii=False
- [{key:vlaue},{key:value}] indent=size





- json.dump():데이터를 json형태로 인코딩(문자열)
- json.dimp():데이터를 json형태로 인코딩하여 파일에 출력(파일)
- ensure_ascii=False
- [{key:vlaue},{key:value}] indent=size

- 정규표현식 -.모든 문자 - *0번이상 반복 -? 있어도 되고 없어도 된다 -<a href="(,*?)"> -<a,*?





### -json 파일 생성

```python
with open('booklist_json.json',mode='w',encoding='utf-8')as file:
        data=[]
        for partial_html in re.findall('<td class="left"><a.*?</td>',html):
            #print(partial_html)
            search=re.search(r'<a href="(.*?)">' ,partial_html).group(1)
            url='http://www.hanbit.co.kr'+search
            
            title=re.sub( r'<.*?>','',partial_html)
            
            data.append({'bookName':title,'link':url})
            print(json.dumps(data,ensure_ascii=False,indent=2))
            
        json.dump(data,file,ensure_ascii=False,indent=2)
```

