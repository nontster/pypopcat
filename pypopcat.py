import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://popcat.click/")
time.sleep(3)

assert "POPCAT" in driver.title

cat = driver.find_element_by_id("app")

while True:
  try:
    cat.click()
  except Exception as ex: # until it breaks
    print('Time is over')
    break

driver.close()