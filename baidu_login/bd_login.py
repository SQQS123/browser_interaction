import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


usrname = 'your_username'
pwd = 'your_pwd'


# 初始化一个浏览器
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
wait = WebDriverWait(browser, 10)


# 得到登录按键,但是在这之前得先输入一些东西，否则不行，因为网页上有两个lb的登录，搜索之后下面得到的是第一个，也就是搜索之后显示的网页的登录按键
button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='u1']/a[@class='lb']")))
button.click()
usrnamelg = wait.until(EC.element_to_be_clickable((By.ID,'TANGRAM__PSP_10__footerULoginBtn')))
usrnamelg.click()


#  模拟登录，如果把随机的阈值设置为0.5那么会被判定为机器，设为0.6则可以成功登录
usrinpt = wait.until(EC.element_to_be_clickable((By.ID,'TANGRAM__PSP_10__userName')))
# 模拟人输入
for i in usrname:
    usrinpt.send_keys(i)
    a = random.uniform(0.2, 0.8)
    time.sleep(a)


pwdinpt = wait.until(EC.element_to_be_clickable((By.ID,'TANGRAM__PSP_10__password')))
# 模拟人输入
for i in pwd:
    pwdinpt.send_keys(i)
    a = random.uniform(0.2, 0.8)
    time.sleep(a)
loginbtn = wait.until(EC.element_to_be_clickable((By.ID,'TANGRAM__PSP_10__submit')))
loginbtn.click()
