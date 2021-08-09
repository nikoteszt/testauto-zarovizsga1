from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"
driver.get(URL)

# használt WebElemek
email_field = driver.find_element_by_id("email")
email_submit = driver.find_element_by_id("submit")


# email mezőt kitöltő függvény
def email_send(address):
    email_field.clear()
    email_field.send_keys(address)
    email_submit.click()
    return


# validációs üzenet kiszedő függvény
def e_val_error():
    val_error = driver.find_element_by_class_name("validation-error").text
    return val_error


# TC01 : Helyes kitöltés esete
email_send("teszt@elek.hu")
time.sleep(2)

# TC02 : Helytelen
email_send("teszt@")
assert e_val_error() == "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes."
time.sleep(2)

# TC03 : Üres
email_send("")
assert e_val_error() == "Kérjük, töltse ki ezt a mezőt."
time.sleep(2)

driver.close()
driver.quit()
