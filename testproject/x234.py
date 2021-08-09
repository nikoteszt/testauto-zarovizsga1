from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"
driver.get(URL)

# WebElemek és tesztadatok

a_input = driver.find_element_by_id("a")
b_input = driver.find_element_by_id("b")
calc = driver.find_element_by_id("submit")
res = ""
negative_res = "NaN"


def cal_fo(a, b):
    global res
    a_input.send_keys(a)
    b_input.send_keys(b)
    calc.click()
    res = driver.find_element_by_id("result").text
    return


# TC01 : Üres kitöltés

a_input.clear()
b_input.clear()
cal_fo("", "")
assert res == negative_res
time.sleep(2)

# TC02 : Nem számokkal történő kitöltés

cal_fo("kiskutya", 12)
assert res == negative_res
time.sleep(2)

# TC03 : Helyes kitöltés esete

a_input.clear()
b_input.clear()
cal_fo(99, 12)
assert res == "222"
time.sleep(2)

driver.close()
driver.quit()
