from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

import globalvars, dictionary_datastructure, fieldnotes, chrome_driver

class post_data():
    def __init__(self):

        # import global variables
        globalvars.init()

        chrome_driver
        # simuate a chrome browser
        driver = webdriver.Chrome(service=globalvars.service)
        # access BrM website
        driver.get('https://brm.kytc.ky.gov/BrM6/Login.aspx?ReturnUrl=%2fBrM6%2fExpiration.aspx')
        # login into the website
        username_driver = driver.find_element(By.ID, "userid")
        username_driver.send_keys(globalvars.username)
        password_driver = driver.find_element(By.ID, "password")
        password_driver.send_keys(globalvars.password)
        login_driver = driver.find_element(By.ID, "btnSignIn")
        login_driver.click()


        for i in range(len(globalvars.bridgeID)):
            # generate an empty dictionary
            bridge_dict = dictionary_datastructure.generate_dict()
            print(globalvars.bridgeID[i])
            # import the field notes
            field_notes = fieldnotes.get_data(i, bridge_dict)
            if i == 0:
                break
            # generate an empty dictionary
            #bridge_dict = dictionary_datastructure.generate_dict()
            # update the dictinary for bridgeID
            #bridge_dict['Structure ID'][1] = globalvars.bridgeID[i]
            # update the dictionary based on condition page
            #get_condition.main(driver, bridge_dict, i)
            # create the Excel field note
            #newExcel.field_notes.create(bridge_dict)



        # close driver
        driver.close()