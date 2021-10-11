# 스파르타 코딩 1일차





- 하나만 꼭! 기억하기!

  ```  HTML 은 뼈대 ``` ```css 는 꾸미기``` ```javascript 는 움직이게``` 하는것!!

  

- Visual Studio code: 코딩을 쉽게 편하게 도와주는 툴 '메모장'같은것!







### 1. html이란?

- 바탕 화면에 xmas 폴더를 생성
- visual studio code에 들어가서 xmas폴더를 오픈  (실행:ctrl +s /ctrl+alt+n)
- html:5를 입력하고 전체 구조를 확인한다.



```python
*아주 기본적인 html 구조당

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```





### 2. 간단한 로그인

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>로그인페이지</title>     #제목
</head>
<body>
    <h1>로그인 페이지</h1>             #바디에 써지는 글귀
    <p>ID: <input type="text"/></p>  # 한줄 뛰고 ID칸
    <p>PW: <input type="text"/></p>  # 한줄 뛰고 PW칸
    <button>로그인하기</button>        # 버튼 생성
</body>
</html>
```



  



### 3. CSS기초

- class 지정

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>로그인페이지</title>
    <style>
        .mytitle{                #.mytitle로 클래스 지정
           color: red 			#지정한 클래스 스타일을 꾸미기
        }
    
    </style>
</head>
<body>
    <h1 class="mytitle">로그인 페이지</h1>  #클래스를 지정!!
    <p>ID: <input type="text"/></p>
    <p>PW: <input type="text"/></p>
    <button>로그인하기</button>
</body>
</html>
```





### 4. 로그인 페이지



```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>로그인페이지</title>          #제목을 지정
    <style>
        .mytitle{					  #첫번째 클래스로 이미지 부분!
            

            width:300px;
            height:200px;

            color:white;
            text-align: center;

            background-image: url('https://www.ancient-origins.net/sites/default/files/field/image/Agesilaus-II-cover.jpg');  #이미지넣기
            background-size: cover;
            background-position: center;         #background 3가지 항상 함께 다님
            
            border-radius: 10px;				#표면 둥글게!
        
            padding-top:20px;                   #안쪽 여백
        }

        .wrap {									#두번째 클래스_중간으로 오게 지정
           
            width:300px;
            margin:auto;

        
        }
    </style>
    
</head>
<body>
    <div class="wrap">           #mytitle전체를 div로 묶어서 wrap클래스로 지정함
        <div class ="mytitle">
            <h1>로그인 페이지</h1>
            <h5>아이디,비번 입력해주세요</h5>
    
    
        </div>
        
        <p>ID: <input type="text"/></p>
        <p>PW: <input type="text"/></p>
        <button>로그인하기</button>
    </div>
    
</body>
</html>
```



완성!! 짝짝!!



<img src="C:\Users\김연희\Desktop\TIL\05_스파르타코딩\img_s\login.JPG" alt="login" style="zoom:33%;" />



