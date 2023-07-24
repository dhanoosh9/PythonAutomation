from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from Patient import AddPatient
BaseCase.main(__name__, __file__)

class PatientTest(BaseCase):
    def test_patient(self):
       AddPatient.create_patient(self) 
