from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
BaseCase.main(__name__, __file__)
import time
from Login import *
from faker import Faker


class AddPatient(BaseCase):
    def create_patient(self):
        faker = Faker()
        # random_first_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(7))
        # random_last_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        # random_email = random_first_name + "@gmail.com"
        LoginInto.login(self)
        self.click("//div[normalize-space()='Process']", By.XPATH, 5)
        self.click("//a[normalize-space()='Patients']", By.XPATH, 5)
        self.click("//button[normalize-space()='Add']", By.XPATH, 5)
        self.select_option_by_text("salutation", "Mr", By.ID, 5)
        self.send_keys("firstName", faker.first_name(), By.ID, 5)
        self.send_keys("lastName", faker.last_name(), By.ID, 5)
        self.select_option_by_index("type", 1, By.NAME)
        self.select_option_by_text("source", "Referal Provider", By.ID, 5)
        self.send_keys("dob", "02021995", By.ID, 5)
        self.select_option_by_text("gender", "Male", By.NAME, 5)
        self.select_option_by_index("maritalStatus", 1, By.ID, 5)
        self.send_keys("homePhone", "4868466484", By.ID, 5)
        self.send_keys("email", faker.email(), By.ID, 5)
        self.send_keys("mobilePhone", "8986255248", By.ID, 5)
        self.click("button.btn.btn-primary", By.CSS_SELECTOR, 5)
        self.select_option_by_text("addressType", "Home", By.NAME, 5)
        self.send_keys("addressLine1", "42", By.NAME, 5)
        self.send_keys("addressLine2", "Todds Lane", By.NAME, 5)
        self.send_keys("city", " Olustee", By.NAME, 5)
        self.select_option_by_index("state", 1, By.NAME, 5)
        self.send_keys("zip", "35635", By.NAME, 5)
        self.select_option_by_index("country", 1, By.NAME, 5)
        self.click("//button[text()='Save & Close']", By.XPATH, 5)
        time.sleep(2)
        LoginInto.logout(self)
        
        
