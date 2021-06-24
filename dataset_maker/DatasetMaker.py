# DatasetMaker by Jason Inirio
# Just run and get a feasible dataset of whatever you want!

#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

# test_url = 'https://www.google.com/search?q=guppies&hl=en&tbm=isch&source=hp&biw=929&bih=932&ei=aTLJYPjqOL-w0PEP9OeciAQ&oq=guppies&gs_lcp=CgNpbWcQAzIFCAAQsQMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BggAEAUQHjoGCAAQChAYUIoMWJkdYMgeaAZwAHgAgAE6iAHeA5IBATmYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAA&sclient=img&ved=0ahUKEwi4w4Os4JrxAhU_GDQIHfQzB0EQ4dUDCAc&uact=5'
dataset_target = input("Input a thing you want to create a dataset for: ")
dataset_size = input("How much of it do you want (good models use 1000+): ") # currently have not tested this

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