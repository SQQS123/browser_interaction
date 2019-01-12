import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


usrname = '17513257267'
pwd = '741WHITESQ'


# 初始化一个浏览器
browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)

# 得到登录按键,但是在这之前得先输入一些东西，否则不行，因为网页上有两个lb的登录，搜索之后下面得到的是第一个，也就是搜索之后显示的网页的登录按键
button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='site-nav-sign']/a[@class='h']")))
button.click()
usrnamelg = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='quick-form']/div/div[@class='login-links']/a[contains(@class,'J_Quick2Static')]")))
usrnamelg.click()



#  模拟登录，如果把随机的阈值设置为0.5那么会被判定为机器，设为0.6则可以成功登录
usrinpt = wait.until(EC.element_to_be_clickable((By.ID,'TPL_username_1')))
# usrinpt.send_keys(usrname)
# 模拟人输入
for i in usrname:
    usrinpt.send_keys(i)
    a = random.uniform(0.3, 0.6)
    time.sleep(a)

time.sleep(2)
pwdinpt = wait.until(EC.element_to_be_clickable((By.ID,'TPL_password_1')))
# pwdinpt.send_keys(pwd)
# 模拟人输入
for i in pwd:
    pwdinpt.send_keys(i)
    a = random.uniform(0.5, 0.6)
    time.sleep(a)
# loginbtn = wait.until(EC.element_to_be_clickable((By.ID,'J_SubmitStatic')))
# loginbtn.click()
