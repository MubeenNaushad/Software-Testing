from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(3)

try:
    # log in
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(4)

    # verify landing on inventory page
    assert "inventory.html" in driver.current_url

    # add backpack to cart and view cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    time.sleep(4)

    print("Script: PASSED")
except Exception as e:
    print(f"Script: FAILED ({e})")
finally:
    driver.quit()
