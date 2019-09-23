import time

from selenium import webdriver
from selenium.webdriver import ActionChains

path = 'driver/chromedriver.exe'

brower = webdriver.Chrome(path)

url = 'https://qzone.qq.com'

brower.get(url)

time.sleep(5)

iframe = brower.find_element_by_xpath('//iframe')
brower.switch_to.frame(iframe)

brower.find_element_by_id('switcher_plogin').click()

account = '870815471'
pwd = 'loser19960207?'

form = brower.find_element_by_id('loginform')
account_element = form.find_element_by_xpath('./div[1]/div/input')
pwd_element = form.find_element_by_xpath('./div[2]/div/input')
submit_element = form.find_element_by_xpath('./div[last()]/a')
account_element.send_keys(account)
pwd_element.send_keys(pwd)
time.sleep(1)
submit_element.click()

time.sleep(10)


iframe = brower.find_element_by_xpath('//iframe')
brower.switch_to.frame(iframe)

slide_element = brower.find_element_by_id('tcaptcha_drag_thumb')

slider = ActionChains(brower)
slider.click_and_hold(slide_element).perform()
slider.reset_actions()
slider.move_by_offset(180,0).perform()
slider.reset_actions()
time.sleep(0.5)
slider.release().perform()

time.sleep(5)

ul_list = brower.find_element_by_id('tab_applist_show')
print(ul_list.tag_name)
time.sleep(1)
li = ul_list.find_element_by_xpath('./li[3]')
li.click()

# farm = ul_list.find_element_by_xpath('./li[3]/')
# farm.click()


time.sleep(5)








