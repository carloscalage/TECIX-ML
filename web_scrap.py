import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url="https://www.sweetwater.com/c987--Classical_and_Nylon_String_Guitars"

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--start-maximized')
options.add_argument('--start-fullscreen')
options.add_argument('--single-process')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--incognito")
options.add_argument('--disable-blink-features=AutomationControlled')
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

driver.get(url)

driver.find_element(By.XPATH, "//button[@class='ccpa-content_cta-button']").click()
driver.find_element(By.XPATH, "//span[@class='site-contact-preview__close']").click()

WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id='ccpa-cookie']")))

driver.find_element(By.XPATH, "//div[@class='product-card__info']//h2//a").click()

name = driver.find_elements(By.XPATH, "//h1[@class='product__name']//span")

for i in name:
  print(i.text)



#teste = driver.find_elements(By.XPATH, "//div[@class='product-card__info']//h2//a")

#for guitar in teste:
#  guitar.click()

#driver.quit()