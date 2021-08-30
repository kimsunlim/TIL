#셀레니움 자동화-구글에서 로그인하고 메일보내기

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url ='https://google.com'
driver.get(url)
action = ActionChains(driver)


driver.find_element_by_css_selector('.gb_3 gb_4 gb_9d gb_3c').click()

#아이디 입력
action.send_keys('rlatjsfla15@gmail.com').perform()
action.reset_actions()
driver.find_element_by_css_selector('.CwaK9').click()


time.sleep(2)
#비밀번호 입력
driver.find_element_by_css_selector('.whOnd.zHQkBf').send_keys('1234')
driver.find_element_by_css_selector('.CwaK9').click()

time.sleep(2)
#메일칸으로 이동
driver.get('https://mail.google.com/mail/u/0/?ogbl#')

#편지쓰기 누르기

driver.find_element_by_css_selector('.T-I T-I-KE L3').click()
time.sleep(1)

send_button = driver.find_element_by_css_selector('.gU.Up')

#받는사람 입력-액션체인스 이용
# 탭을 누르면 제목으로 이동!! 한번누르면 이메일한번더 추가 두번누르면 제목칸으로 이동
(action.send_keys('rlatjsfla15@gamil.com').key_down(Keys.TAB)
 .key_down(Keys.TAB).send_keys('제목입니다.')
 .key_down(Keys.TAB).send_keys('내용입니다.')
 .move_to_selement(send_button).click() #보내기 누르기
 .perform())




