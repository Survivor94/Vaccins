from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keys

def createDriver():
    # Create the driver with options
    options = webdriver.ChromeOptions()

    # Exclude the top bar of driver automation
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])

    # Standard arguments
    options.add_argument("window-size=1280,800")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

    # Give the driver some brains, to remember not to login every time
    options.add_argument("user-data-dir=/home/ubuntu/Desktop/Vaccins/~")

    # Search for the chromedriver
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)

    # Open the given website
    driver.get("https://www.prullenbakvaccin.nl/")
    
    return driver

def standardLogin(driver, codes):

    # Search for login field
    driver.implicitly_wait(10)
    chooseLocation = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/form/input[2]")
    chooseLocation.send_keys(Keys.CONTROL + "a")
    chooseLocation.send_keys(Keys.DELETE)
    chooseLocation.send_keys(codes)
    driver.implicitly_wait(5)
    submitLocation = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/form/button").click()
    
    return driver

def textFunc(driver):
    # Click accept of login field
    driver.implicitly_wait(10)
    searchLocations = driver.find_element_by_xpath("/html/body/main/div[2]/div[3]/div[1]/h2").text
    amount = searchLocations[0]

    return amount

