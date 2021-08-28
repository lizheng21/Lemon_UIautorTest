from selenium import webdriver
import time
from data import test_data
from method import test_method

driver = webdriver.Chrome()  # 启动浏览器

# 打开具体的网址
driver.get("http://erp.lemfix.com/login.html")
# 窗口最大化
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(10)
username = test_data.data1.get("name")
password = test_data.data1.get("passwd")
keys = test_data.data1.get("key")
test_method.login(driver, username, password)
number = test_method.search(driver, keys)
if keys in number:
    print("成功！")
else:
    print("失败!")
