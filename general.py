import time
import selenium
import os
import random
from PIL import Image , ImageEnhance
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class Parcer():

    def __init__(self, link, klas):
        self.link = link
        self.klas = klas
        self.driver = webdriver.Chrome()
        self.driver.get(self.link)



    def getlinks(self):
        elements_first_page = self.driver.find_elements(By.CLASS_NAME, self.klas)
        links_list = []
        for element in elements_first_page:
            href = element.find_element(By.TAG_NAME, 'a')
            url = href.get_attribute('href')
            links_list.append(url)

        for links in links_list:
            self.driver.get(links)
            tabs = self.driver.find_elements(By.CLASS_NAME, 'product-tabs__btn')

            for tab in tabs:
                if 'Характеристики' in tab.text:
                    self.driver.execute_script("arguments[0].click();", tab)
                    time.sleep(2)



    def go_to_next_page(self):
        click_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "show-more"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", click_element)

        time.sleep(3)
        click_element.click()

        time.sleep(5)

        









