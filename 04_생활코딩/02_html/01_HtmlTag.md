# HTML 1일차

1. web의 핵심적인 철학은 접근성이다.
2. web모든 운영체제에서 동작하고
3. web의 소스코드는 누구나 볼수있고
4. web은 저작권이 없는 순수한 공공재이다.





#### 1) 태그

- web을 지배하는 문법 태그!!

```python
#글씨 진하게 강조
<strong>creating web pages </strong>

#web부분 밑줄로 더 강조!
<strong>creating <u>web</u> pages </strong>

```







#### 2) 속성과 img

- 태그의 이름만으로는 정보가 부족 그래서 속성(attribute) 도입
- src=속성 :속성을 통해서 더 많은 의미를 부과 할 수 있음

```python 
<img src="coding.jpg" width="100%">
```





#### 3)부모 자식과 목록

```python
<parent>			# 부모태그
	<child></child>  #자식태그
</parent>
```



  **즉!**

```python
<p>
	<a href="https://opentutorials.org">opentutorials</a>
</p>
```

 

- 필요에 따라서 관계가 달라 질수 있다.

- 그런데 몇몇 태그들은 부모-자식 관계처럼 고정된 관계의 태그들이 있음

- ul은 그룹핑 하기 위해서 li태그의 부모태그다! 항상 같이 있어야함

```python
#목차   li태그의 부모태그!!
<ul>				
    <li>1. HTML</li>
    <li>2. CSS</li>
    <li>3. JavaScript</li>
</ul>
```



- ol태그를 쓰면 목차에 자동으로 넘버링 됨

```python
<ol>				
    <li> HTML</li>
    <li> CSS</li>
    <li> JavaScript</li>
</ol>
```





#### 4) 문서의 구조



1. 제목

```python
<title> WEB </title>
```



2. UTF-8  :글씨 안깨지게

```python
<meta charset="utf-8">
```

 :영어가 아닌 문자가 깨지는 이유는 웹페이지가 저장된 문자 표현 방식과
 웹브라우저가 웹페이지를 해석하는 방식이 일치하지 않을 때 웹브라우저는 저렇   게 이상한 문자를 표시



3. html[본문은**body**, 본문을 설명하는 태그는**head**]

- doctype html  :html 타입이다.

```python
<!doctype html>
<html>
<head>
  <title>WEB1 - html</title>
  <meta charset="utf-8">
</head>
<body>
  <ol>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
  </ol>
  <h1>HTML</h1>
  <p>Hypertext Markup Language (HTML) is the standard markup language for <strong>creating <u>web</u> pages</strong> 
```





#### 5) HTML 태그 제왕

 

>  바로 링크 **link**  `<a>`



```python
#<a>는 링크
#href는 참조

<p><a href="https://www.w3.org/TR/html5/" target="_blank" title="html5 specification">Hypertext Markup Language (HTML)</a> 
```



