from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from credentials import username, password

CHROME_DRIVER_PATH = "../chromedriver.exe"
SIMILAR_ACCOUNT = ""
USERNAME = username
PASSWORD = password


class InstaFollower:
    def __init__(self):
         self.s = Service("../chromedriver.exe")
         self.driver = webdriver.Chrome(service=self.s)
    
    