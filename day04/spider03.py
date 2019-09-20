import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC

path = 'driver/chromedriver.exe'

# 创建浏览器
brower = webdriver.Chrome(path)

# 打开网站
def start():
    brower.get("https://www.baidu.com")

    title1 = brower.title
    title2 = brower.find_element_by_xpath('//title').text
    print(title1)
    print(title2)

    # 搜索dockerEs集群
    kwElement: WebElement = brower.find_element_by_id('kw')
    kwElement.send_keys('dockerEs集群')
    button = brower.find_element_by_id('su').click()
    while True:
        parse()
        time.sleep(2)
        brower.find_element_by_css_selector('#page').find_element_by_xpath('./a[last()]').click()

def parse():
    num = brower.find_element_by_class_name('nums_text').text
    print(num)
    # content = brower.find_elements_by_id('content_left')
    h3_list  = brower.find_elements_by_tag_name('h3')
    for h3element in h3_list:
        title = h3element.find_element_by_xpath('./a')
        print(title.text,title.get_attribute('href'))
if __name__ == '__main__':
    start()
