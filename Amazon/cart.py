from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
try:
    driver.maximize_window()
    # direct link to a product
    driver.get("https://www.amazon.com/dp/B08N5WRWNW/")
    time.sleep(5)  # wait for page load

    # click "Add to Cart"
    driver.find_element(By.ID, "add-to-cart-button").click()
    time.sleep(3)

    # sometimes a popup appears, attempt to close it
    try:
        driver.find_element(By.XPATH, "//span[@id='attach-close_sideSheet-link']").click()
        time.sleep(1)
    except:
        pass

    # verify cart URL contains "cart"
    assert "cart" in driver.current_url, "Did not navigate to cart page."
    print("Add to Cart test: PASSED")
    
except Exception as e:
    print(f"Add to Cart test: FAILED ({e})")
finally:
    driver.quit()
