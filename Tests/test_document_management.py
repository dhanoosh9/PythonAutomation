from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
BaseCase.main(__name__, __file__)
from DocumentManagement import *

class DocumentManagementTest(BaseCase):
    def test_document_upload(self):
        DocumentManagement.file_upload(self)
