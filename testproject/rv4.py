from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"
driver.get(URL)

# Kivesszük a textarea-ból a "létező" városokat egy listába
real_cities = driver.find_element_by_id("cites").text
r_cities = real_cities.strip('"').split('", "')
print(r_cities)

# Kivesszük a random listában levő városokat egy másik listába
random_cities = driver.find_elements_by_xpath('//ul[@id="randomCities"]/li')
rand_cities = []
for j in range(len(random_cities)):
    rand_cities.append(random_cities[j].text)
print(rand_cities)



driver.close()
driver.quit()
