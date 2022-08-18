from selenium import webdriver
from selenium.webdriver.common.by import By

# 계정정보 입력
id = 'personar95'
password = '12344565'
# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome('./ref/chromedriver.exe')

# 네이버 로그인 페이지 접속
driver.get('https://nid.naver.com')

# 아이디 입력
input_id = driver.find_element(By.CSS_SELECTOR, 'input#id')
input_id.send_keys(id)

# 비밀번호 입력
input_password = driver.find_element(By.CSS_SELECTOR, 'input#pw')
input_password.send_keys(password)

# 로그인 버튼 클릭
login = driver.find_element(By.ID, 'log.login')
login.click()