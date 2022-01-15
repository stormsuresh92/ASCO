from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.headless=True

driver = webdriver.Firefox(executable_path=r'E:\Webdriver\geckodriver.exe', options=options)
driver.get('https://meetinglibrary.asco.org/record/201990/abstract')
driver.implicitly_wait(20)
title = driver.find_element_by_xpath('.//h1[@class="ng-tns-c11-2"]')
author = driver.find_element_by_xpath('.//div[@class="authors"]')
abstract = driver.find_element_by_xpath('.//div[@class="abstract-content"]')

print(title.text, author.text, abstract.text)