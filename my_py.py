from selenium import webdriver
from time import sleep

browser = webdriver.Chrome(executable_path="C:/Users/BenAzoulay/PycharmProjects/DevOpsCourse/Lesson 4/my_selenium"
                                           "/chromedriver/chromedriver.exe")

browser.get('http://www.walla.co.il')
sleep(1)

browser.close()
