# DatasetMaker by Jason Inirio
# Just run and get a alright dataset of whatever you want!

#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

dataset_target = input("Input a thing you want to create a dataset for: ")
dataset_size = input("How much of it do you want (good models use 1000+): ") # currently have not tested this and does not work right now

#Opens up web driver and goes to Google Images
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://images.google.com/')

# Now let's get the search bar
box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
# print(dataset_target)
box.send_keys(dataset_target)
box.send_keys(Keys.ENTER)

# 'sort of' infinite loop to get all the images
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    
    last_height = new_height

for i in range(1, int(dataset_size)):
    try:
        print("on image " + str(i))
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img').screenshot('Dataset Output/' + str(dataset_target) + '_' + str(i) + '.png')
    except:
        pass