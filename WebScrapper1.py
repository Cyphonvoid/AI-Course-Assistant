from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time


#Path to web driver
PATH = "chromedriver.exe"

serv = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=serv)

#URl to use from
url = {
    'google' : "https://www.google.com",
    "nasa": "https://www.nasa.gov/earth/climate-change/as-the-arctic-warms-its-waters-are-emitting-carbon/"
}


#Just getting the page of the url
driver.get(url["nasa"])


#Getting the headline
element_headline = driver.find_element(By.XPATH, value='//*[@id="post-583846"]/section/div[1]/div[2]/div/div/div/h1')
headline = element_headline.text 

#print("Article Headline: ", headline)


#Getting article contact information
contact = driver.find_element(By.XPATH, '//*[@id="post-583846"]/section/div[2]/div[2]/div/p[15]')
contact_info = contact.text

#print("\nContact Info: ", contact_info)


#Getting the author
author = driver.find_element(By.XPATH, '//*[@id="post-583846"]/section/div[2]/div[2]/div/p[16]')
author_info = author.text

#print("\nAuthor Info: ", author_info)


#Getting the date of the article
date = driver.find_element(By.XPATH, '//*[@id="post-583846"]/section/div[2]/div[1]/div[2]')
date_info = date.text

#print("\nDate Published: ",date_info)



#Getting other links to articles
article_data = []
for i in range(1, 4):
    Str = '//*[@id="post-583846"]/section/div[4]/section/div[2]/div[' + str(i) + ']'
    article_data.append(driver.find_element(By.XPATH, Str).text)
    print("External Article :",i,article_data[i-1])




#Getting miscllenous data
misc = driver.find_element(By.XPATH, '/html/body/footer/div')
misc_info = misc.text


page_data = {
    'heading':headline,
    'contact':contact_info,
    'author':author_info,
    'other_articles':article_data[0] + article_data[1] + article_data[2],
    'other_data':misc_info,
}

#Writing data to file,
file = open("Data.json", "r")
file_data = json.load(file)

file_data["details"] = page_data #Change details to something else if that's where you wanna store data
file.close()

file = open("Data.json", "w")
file.write(json.dumps(file_data, indent=4))



#quiting
driver.quit()


