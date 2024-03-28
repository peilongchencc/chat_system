from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import urllib.request

path = 'C:\Program Files\Google\Chrome\Application\chromedriver'
browser = webdriver.Chrome(path)

url='https://baijiahao.baidu.com/s?id=1793832549445442560'
browser.get(url)
time.sleep(5)
title=browser.find_element_by_xpath('//*[@id="header"]/div[1]').text
content=browser.find_element_by_xpath('//*[@id="ssr-content"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/p').text
img_url=browser.find_element_by_xpath('//*[@id="ssr-content"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div/img').get_attribute('src')
urllib.request.urlretrieve(img_url,'img.jpg')
with open('data.txt','w',encoding='utf-8')as fp:
    fp.write(str(title)+'\n')
    fp.write(str(content) + '\n')
print(title)
print(content)
print(img_url)
browser.close()