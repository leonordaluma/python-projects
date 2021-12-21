from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = "../chromedriver.exe"
s = Service("../chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://en.wikipedia.org/wiki/Main_Page")


article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(article_count.text)
driver.quit()