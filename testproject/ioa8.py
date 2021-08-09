from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import operator

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"
driver.get(URL)

# Szükséges WebElemek
number_1 = driver.find_element_by_id("num1").text
number_2 = driver.find_element_by_id("num2").text
cal_operator = driver.find_element_by_id("op").text
cal_button = driver.find_element_by_id("submit")

# cal_operator beazonosításához szükséges
operator_lookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
op = operator_lookup.get(cal_operator)

# Számolás pythonnal
py_cal_result = op(int(number_1), int(number_2))
print("result is (python): ", py_cal_result)

# Applikáció számolássa
cal_button.click()
app_cal_result = driver.find_element_by_id("result").text
print("result is (applikacio):", app_cal_result)

# A két számolás összevetése
assert str(py_cal_result) == app_cal_result
print("Heuréka, egyeznek :)")

time.sleep(3)
driver.close()
driver.quit()
