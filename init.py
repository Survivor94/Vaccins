from selenium import webdriver
from time import sleep
import login
import telegrambot
import time

# Zip codes
zip = ["3571AB", "3822TB"]
timeOutZip = []
timeOutTime = []

# Perform login
driver = login.createDriver()

while(True):
    try:
        if timeOutZip:
            for removedItems in range(0,len(timeOutTime)):
                if(time.time() >= timeOutTime[removedItems]):
                    zip.append(timeOutZip[removedItems])
                    timeOutZip.remove(timeOutZip[removedItems])
                    timeOutTime.remove(timeOutTime[removedItems])
    except:
        pass

    for codes in zip:
        driver = login.standardLogin(driver, codes)
        amount = login.textFunc(driver)
        if amount == "0":
            pass
        else:
            try:
                if zip:
                    # Check of er echt iets is.
                    driver.implicitly_wait(10)
                    vaccinAvailability = driver.find_element_by_xpath("/html/body/main/div[2]/div[3]/div[2]/div[2]/div/div/div/h5/small").text
                    if vaccinAvailability != "Heeft geen vaccins":
                        zip.remove(codes)
                        telegrambot.initiateChat(codes)
                        timeOutZip.append(codes)
                        timeOutTime.append(time.time() + 3600)
                    else:
                        pass
                else:
                    time.sleep(3600)
            except:
                pass
        time.sleep(20)
        driver.refresh()