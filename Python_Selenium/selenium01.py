##selenium및 웹드라이버 설치


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)

#검색창에 '파이썬'입력하기/ 엔터누르기
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('파이썬') #문자 입력
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)

#'파이썬 위키백과'글 들어가보기

#driver.find_element_by_css_selector('.LC201b').click()

#두번째나 세번째 게시글 들어가보기_리스트로 위치 지젇
driver.find_elements_by_css_selector('.LC20lb')[2].click()