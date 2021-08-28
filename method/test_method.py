def login(driver, user, password):
    # 元素定位方法：id，name,xpath(重点)
    username = driver.find_element_by_id("username")
    # 进行操作：输入内容
    username.send_keys(user)
    driver.find_element_by_id("password").send_keys(password)
    # 点击操作
    driver.find_element_by_id("btnSubmit").click()


def search(driver, key):
    # xpath 页面里面copy路径，元素在html页面里的路径
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    # 寻找到子页面
    frameId = driver.find_element_by_xpath('//span[text()="零售出库"]/..').get_attribute("data-tab-id")
    frameId = frameId + "-frame"
    driver.switch_to.frame(frameId)
    driver.find_element_by_id("searchNumber").send_keys(key)
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]//div').text
    driver.find_element_by_id("searchBtn").click()
    return num
