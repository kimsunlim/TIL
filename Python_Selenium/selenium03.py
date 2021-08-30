#셀레니움 새탭열고 닫는 법

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')

time.sleep(2)

# 창 열기
driver.execute_script('window.open("https://naver.com");')  #자바 스크립 형식으로 새탭 여는것
time.sleep(1)

driver.execute_script('window.open("https://daum.net");')
time.sleep(1)

driver.execute_script('window.open("https://daum.net");')
time.sleep(1)

#창전환// 팝업창 생겼을 때 쓰기 유영
driver.switch_to_window(driver.window_handles[0])
time.sleep(1)

#창닫기
driver.close()

