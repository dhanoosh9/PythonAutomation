from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
BaseCase.main(__name__, __file__)
import time


class LoginInto(BaseCase):
    def login(self):
        self.open("http://183.82.123.57:3000/login")
        self.maximize_window()
        self.send_keys('email', 'admin', By.NAME, 10)
        self.send_keys('password', '123qwe', By.NAME, 10)
        self.click("button")
        self.wait(2)
        self.select_option_by_text("facility","Apollo",By.ID,10)
        self.select_option_by_text("roles","ADMIN",By.ID,10)
        self.click("button")
        self.wait(5)
        self.click("user", By.CLASS_NAME, 5)
    def logout(self):
        #self.click("//img[src='./images/unknown_user.png']", By.XPATH)
        # self.click("//div[@title='User Info']", By.XPATH, 10)
        # self.click("//div[@title='User Info']", By.XPATH, 10)
        self.js_click("//div[@title='User Info']", all_matches=True)
        self.js_click("//a[text()='Logout']", all_matches=True)
        # self.click("//li/a[text()='Logout']", By.XPATH, 10)
        


        

        
