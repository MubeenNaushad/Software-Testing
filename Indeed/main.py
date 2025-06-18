from selenium import webdriver
import undetected_chromedriver as uc #to bypass captcha
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = uc.Chrome()
driver.maximize_window()

driver.get("https://www.indeed.com/")

time.sleep(5)

try:
    driver.find_element(By.ID, "text-input-what").send_keys("Software Tester")
    driver.find_element(By.ID, "text-input-what").send_keys(Keys.RETURN)
    time.sleep(15)

    driver.find_element(By.ID, "filter-jobtype1").click()
    driver.find_element(By.ID, "filter-jobtype1-0").click()
    driver.find_element(By.CSS_SELECTOR, "button[form='filter-jobtype1-menu']").click()
    time.sleep(4)

    driver.find_element(By.CSS_SELECTOR, "h2.jobTitle a").click()
    time.sleep(3)

    apply_btn = driver.find_element(By.CSS_SELECTOR, "button[id='indeedApplyButton']")
    assert apply_btn.is_displayed(), "Apply Now button not found or not visible"

    title = driver.find_element(By.CSS_SELECTOR, "h2.jobsearch-JobInfoHeader-title").text
    assert "Software Tester" in title, f"The title does not have 'Software Tester': The title is {title}"

    print("Apply now button is visible and title matches exactly.")

except Exception as e:
    print(f"Error encountered: {e}")
else:
    print("Task successfully completed.")

finally:
    driver.quit()
    print("Code executed, Driver closed.")