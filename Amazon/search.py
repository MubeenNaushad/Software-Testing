from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get("https://www.amazon.com/")
    time.sleep(5)  # wait for page to load

    # perform search
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Computer")
    driver.find_element(By.ID, "nav-search-submit-button").click()
    time.sleep(5)  # wait for results

    # verify
    assert "Computer" in driver.page_source, "Search term not found in results."
    print("Search test: PASSED")
except Exception as e:
    print(f"Search test: FAILED ({e})")
finally:
    driver.quit()
