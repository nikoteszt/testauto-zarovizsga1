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

# A két lista összehasonlítása, megkeressük azt amelyik csak az egyikben van jelen.
exist_city = ""
for k in range(len(r_cities)):
    exist_city = rand_cities.count(r_cities[k])
    if exist_city == 0:
        break

print(f'Yes, "{r_cities[k]}"in city')
hianyzo_varos = r_cities[k]

# Az applikáció által választott várossal való összehasonlítás
driver.find_element_by_id("missingCity").send_keys(hianyzo_varos)
driver.find_element_by_id("submit").click()
assert driver.find_element_by_id("result").text == "Eltaláltad."
print(hianyzo_varos, "Ez jó tipp volt")

time.sleep(2)
driver.close()
driver.quit()
