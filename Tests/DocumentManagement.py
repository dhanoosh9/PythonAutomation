from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
BaseCase.main(__name__, __file__)
import time
from Login import *

class DocumentManagement(BaseCase):
    def file_upload(self):
        LoginInto.login(self)
        self.click("(//li[contains(@class,'menu-item')])[1]", By.XPATH, 5)
        self.click("//a[normalize-space()='Document Management']", By.XPATH, 5)
        self.click("//button[normalize-space()='Add +']", By.XPATH, 5)
        
        self.send_keys("file", r"C:\Users\dhano\Desktop\python\PronixSeleniumPythonFramework\Tests\Sample.pdf", By.ID, 5)
        self.send_keys("patientName", "asher a", By.ID, 5)
        time.sleep(1)
        elements = self.find_elements("dropDownItem", By.CLASS_NAME)
        for element in elements:
            if element.text == 'asher a':
                element.click()
                break
        self.send_keys("description", "sample", By.ID, 5)
        self.click("//button[normalize-space()='Upload']", By.XPATH, 5)
        time.sleep(2)

       