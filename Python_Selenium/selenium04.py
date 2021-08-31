######### 인스타 해시태그 selenium


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os



search_word = input('검색어 입력해:')
tag_n =input('가져올 태그의 숫자를 입력해')

##인스타그램에 입장~ 로그인하기
driver = webdriver.Chrome()
driver.get('https://www.instagram.com')

time.sleep(3)
#로그인
driver.find_element_by_link_text('로그인').click()
login = driver.find_elements_by_css_selector('_2hvTZ pexuQ zyHYP')[0].send_keys('hanmigin26')
login = driver.find_elements_by_css_selector('_2hvTZ pexuQ zyHYP')[1].send_keys('gksalakrm1!')

login.send_keys(Keys.ENTER).perform()
time.sleep(3)


driver.get('https://www.instagram.com/explore/tags/아파트/')
time.sleep(3)


################# 해시태그 크롤링하기

###게시글 클릭

time.sleep(3)

driver.find_elements_by_css_selector('._9AhH0')[0].click()

#해시태그 클릭

tags = driver.find_elements_by_css_selector('xil3i')



#해시 태그 한글당 여러개 있음 그래서 반복문 생성//
#####조건 반복문으로 원하는 범위만큼 진행하기//다음클릭과 해시태그를 불러오는 반복문
#for문을 돌리고 내용을 담을 빈 list만들기

tag_list=[]
n=1

for i in tags:
    print(i.text)
    tag_list.append(i.text)
    n +=1       #몇번째 해시태그인지 알기위해 생성


##조건에 따라 반복하기 위해while True사용
while True:
    try:
        if int( tag_n ) > n:
            driver.find_element_by_link_text('다음').click()  #####다음게시물 클릭
            time.sleep(3)
            tags = driver.find_elements_by_css_selector('xil3i')
            for i in tags:

                print(n) #몇번째 해시태그가 진행중인지 확인
                print(i.text)

                tag_list.append(i.text)
                n+=1


        else:   #if조건에 맞지않는다면 멈추고 /반대라면 n이 우리가 찾고자하는 해시태그의 수보다 크거나 같은경우이다
            if n >= int(tag_n):
                break

            else:       #두조건다 아닌경우가 있음, 다 찾아지지도 않았는데 넘어오는 경우는 스크롤 해주기
                driver.excute_script('window.scrollTo(0,document.body.scrollHeihgt)')

    except:
        if n>= int(tag_n):
            break


print(len(tag_list))


##list를 csv로 저장//데이터 프레임으로 저장

import pandas as pd

insta0 = pd.DataFrame()
insta0[search_word]=tag_list   #우리가 검색한 키워드로 칼럼이름을 만들고 내용담기

insta0.to_csv('insta_tag.csv')



#######원하는 위치에 저장하기

os.chdir('c:\\test\\')  #기본작업위치 변경
insta0.to_csv('insta_tag.csv')  #파일저장









