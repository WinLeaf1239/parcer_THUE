import time
import selenium
import os
import random
from PIL import Image , ImageEnhance
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pandas as pd


class Parcer():

    def __init__(self, link, klas):
        self.link = link
        self.klas = klas
        self.driver = webdriver.Chrome()
        self.driver.get(self.link)
        self.info_list = []
        self.date_dict = {}
    

    def getlinks(self):
        elements_first_page = self.driver.find_elements(By.CLASS_NAME, self.klas)
        links_list = []
        for element in elements_first_page:
            href = element.find_element(By.TAG_NAME, 'a')
            url = href.get_attribute('href')
            links_list.append(url)

        for links in links_list:
            self.driver.get(links + "#characteristics")
            time.sleep(3)
            tabble_list = self.driver.find_elements(By.TAG_NAME, 'td')
            for table in tabble_list:
                self.info_list.append(table.text)
            time.sleep(3)
            

    def creating_csv_file(self):
       
        for i in range(0 , len(self.info_list)-1):
            if (i % 2 == 0):
                self.date_dict.update({self.info_list[i] : [self.info_list[i + 1]]})
                if self.info_list[i] == 'Страна происхождения (производства)*':

                    df_1 = pd.DataFrame(self.date_dict)
                    print(df_1)
                    df_1.to_csv("var.csv", index=False,  mode="a", sep=",", header=not os.path.isfile("var.csv"))
        print(self.date_dict)

    
    def accept_cookie(self):
        click_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "popup-cookie__confirm"))
        )
        click_element.click()
        time.sleep(2)


    def go_to_next_page(self):
        click_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "show-more"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", click_element)

        time.sleep(3)
        click_element.click()

        time.sleep(3)





        









