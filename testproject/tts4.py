from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"
driver.get(URL)

# Előkészítés
toss_up = driver.find_element_by_id("submit")
head_result = 0

# 100 * feldobjuka pénzt, és ahányszor fej lesz az eredmény dobás után, annyiszor növeljük 1-el a head_result számlálót
for i in range(100):
    toss_up.click()
    last_result = driver.find_element_by_id("lastResult").text
    if last_result == "fej":
        head_result += 1

# Akkor elfogadható véletlenszerünek a feldobás, ha legalább 30 esetben fej lesz.
assert head_result >= 30

time.sleep(3)
driver.close()
driver.quit()
