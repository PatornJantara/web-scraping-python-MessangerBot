from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time


def dataCovid():
    global driver
    covid_url = 'https://covid19.th-stat.com/'  # Your target url
    driver.get(covid_url)   # navigate browser to target url
    page = driver.page_source   # get sourcecode of webpage
    soup = bs(page,'html.parser')   # convert page sorucecode into HTML
    # Find all which in specific word
    head = soup.find_all('div',{'class':'block-title-page'}) 
    content = soup.find_all('div',{'class':'block-st-all'})
    message = []
    # soup_find_all will return data in list term
    for sub_head in head:
        message.append(sub_head.text.replace('\n',''))
    for sub_content in content:
        message.append(sub_content.text.replace('\n',''))

    return message

def botMessager(message):
    global driver
    facebook_url = 'https://web.facebook.com/'  
    driver.get(facebook_url) 
    bot_user = 'xxx-xxx-xxx'   # Your bot username
    bot_password = 'xxx-xxx-xxx'         # Your bot password

    # Find element by XPATH (recommendation)
    user = driver.find_element(By.XPATH,'//*[@id="email"]')
    password = driver.find_element(By.XPATH,'//*[@id="pass"]')
    login = driver.find_element(By.XPATH,'//*[@id="u_0_b"]')

    user.send_keys(bot_user)    # Sort text
    password.send_keys(bot_password)
    login.click()   # click
    time.sleep(2)
    my_messager_url = 'xxx-xxx-xxx' # from chatbot side
    driver.get(my_messager_url)
    for sub_message in message :
        messager = driver.find_element(By.XPATH,'//*[@id="js_f"]/div/div/div')
        messager.send_keys(sub_message)
        messager.send_keys(Keys.ENTER)  # Enter
        time.sleep(2)
    driver.quit()

# Set up chromedriver    
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') # ignore any error sending back
options.add_argument('--incognito')     # Incognito mode (un-identify user)
options.add_argument('--headless')      # Dont open up browser

# run chrome-driver 
driver = webdriver.Chrome(r'C:\Users\User\Downloads\chromedriver.exe', chrome_options=options)

message = dataCovid()
botMessager(message)

