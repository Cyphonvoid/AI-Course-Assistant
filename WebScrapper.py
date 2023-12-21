from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openai import OpenAI
import time


#Path to web driver
PATH = "chromedriver.exe"

serv = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=serv)

#URl to use from
url = {
    'google' : "https://www.google.com",
    "nasa": "https://www.nasa.gov"
}


#Just getting the page of the url
driver.get(url["google"])


#printing the title
print("Page Title: ", driver.title)


#waiting
time.sleep(4)


#quiting
driver.quit()


client = OpenAI()
print(client)


