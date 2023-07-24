from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from Login import LoginInto
BaseCase.main(__name__, __file__)


class LoginTest(BaseCase):
    def test_login(self):
        
        LoginInto.login(self)
        LoginInto.logout(self)
        

        
