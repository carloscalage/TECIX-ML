import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Configurations for hidding that we are actually a bot :´)
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--start-maximized')
options.add_argument('--start-fullscreen')
options.add_argument('--single-process')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("disable-infobars")

driver = webdriver.Chrome('./chromedriver')
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })
driver.maximize_window()

url="https://www.sweetwater.com/c987--Classical_and_Nylon_String_Guitars"

# Start the process of entering the page
driver.get(url)

# Clicking on the page's cookie check button and closing contact box
driver.find_element(By.XPATH, "//button[@class='ccpa-content_cta-button']").click()
driver.find_element(By.XPATH, "//span[@class='site-contact-preview__close']").click()
# If the cookie check box is still there, a human should do the job
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id='ccpa-cookie']")))

products = driver.find_elements(By.XPATH, "//h2[@class='product-card__name']//a")

index = 14
q = range(len(products))

for elem in q:
  data = {}
  
  time.sleep(1)
  
  products[index].click()

  time.sleep(1)

  dollars = driver.find_element(By.TAG_NAME, 'dollars').text
  cents = driver.find_element(By.TAG_NAME, 'cents').text
  data['Price']  = dollars + cents

  # Getting all table rows
  table = driver.find_elements(By.XPATH, "//li[@class='table__row']")

  # Getting header and body and appending to data dict
  for i in table:
    data[i.find_element(By.CLASS_NAME, 'table__header').text.replace(':', '')] = i.find_element(By.CLASS_NAME, 'table__cell').text

  print(data)

  driver.back()
  time.sleep(1)
  products = driver.find_elements(By.XPATH, "//h2[@class='product-card__name']//a")
  index += 1
