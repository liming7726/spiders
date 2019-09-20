import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

brower = webdriver.Chrome('driver/chromedriver.exe')




def start():

    #访问智联招聘网站
    brower.get('https://www.zhaopin.com/')
    time.sleep(3)
    #等待智联招聘的弹窗
    brower.find_element_by_class_name('risk-warning__content').find_element_by_xpath('./button').click()

    #切换城市
    city = brower.find_element_by_class_name('zp-city__change').click()
    m = brower.window_handles
    print(m)
    brower.switch_to.window(m[-1])

    #输入切换城市的名称
    city_input = brower.find_element_by_link_text('西安').click()

    # city_input.send_keys('西安')
    # city_input.send_keys(Keys.ENTER)


    #切换窗口
    n = brower.window_handles
    print(n)
    brower.switch_to.window(n[-1])
    time.sleep(5)
    #输入搜索关键字
    input_txt = brower.find_element_by_class_name('zp-search__input')
    input_txt.send_keys('python')
    time.sleep(2)
    brower.find_element_by_class_name('zp-search__btn').click()
    # print('----------------------------------------------------')
    z = brower.window_handles
    brower.switch_to.window(z[-1])


    #等待数据出现
    ui.WebDriverWait(brower,10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME,'a-center-layout'))
    )
    time.sleep(5)

    while True:
        content = brower.find_element_by_id('listContent')
        data_list = content.find_elements_by_xpath('./div')
        for i in data_list[:-2]:
            job = i.find_element_by_xpath('./div/a/div/div/span').text
            trde = i.find_element_by_xpath('./div/a/div[2]/div/p').text
            area = i.find_element_by_xpath('./div/a/div[2]/div/ul/li[1]').text
            age = i.find_element_by_xpath('./div/a/div[2]/div/ul/li[2]').text
            xueli = i.find_element_by_xpath('./div/a/div[2]/div/ul/li[3]').text

            print('职位：%s 待遇：%s 地区：%s 所需工龄：%s 学历：%s'%(job,trde,area,age,xueli))
        brower.execute_script('document.documentElement.scrollTop=100000')
        time.sleep(1)
        brower.find_elements_by_class_name('soupager__btn')[1].click()
        time.sleep(5)
        print('-------------------------下一页---------------------------')
    # brower.quit()





if __name__ == '__main__':
    start()
    # brower.get('https://sou.zhaopin.com/?jl=854&kw=python&kt=3')
    # time.sleep(20)
    # brower.execute_script('document.documentElement.scrollTop=100000')
    # a = brower.find_elements_by_class_name('soupager__btn')[1]
    # print(a.text)
    # b = a.find_elements_by_xpath('./')
    #
    # print(a.text)
    # a.click()

