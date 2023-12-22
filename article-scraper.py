from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openai import OpenAI
import time


# Path to web driver
PATH = "chromedriver.exe"

serv = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=serv)

# URL
URL = "https://www.nasa.gov/earth/climate-change/as-the-arctic-warms-its-waters-are-emitting-carbon/"

# Just getting the page of the url
driver.get(URL)

# Grab the main article text elements
element = driver.find_element(By.CLASS_NAME, "entry-content")

# Grab the "insides" of the html element
text = element.text

print(text)

#waiting
time.sleep(4)

#quiting
driver.quit()
