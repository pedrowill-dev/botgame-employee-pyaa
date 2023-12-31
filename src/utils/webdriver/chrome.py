from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Chrome:

  def __init__(self):
    self.service = Service(ChromeDriverManager().install())
    self.browser = webdriver.Chrome(service=self.service)

  @property
  def get_driver(self):
    return self.browser


