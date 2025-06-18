from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.edx.org")
time.sleep(5)

try:
    # enter search term and submit
    driver.find_element(By.XPATH,
        "/html/body/header/div[1]/div/div[1]/div/div/div[1]/form/div/input"
    ).send_keys("Python Programming")
    time.sleep(3)
    driver.find_element(By.XPATH,
        "/html/body/header/div[1]/div/div[1]/div/div/div[1]/form/div/input"
    ).send_keys(Keys.RETURN)
    time.sleep(5)

    # filter by “Introductory” level
    driver.find_element(By.ID, "Introductory").click()
    time.sleep(5)

    # click the first course result
    driver.find_element(By.XPATH,
        "/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]"
    ).click()
    time.sleep(5)

    # verify enroll-now button and title
    advance_button = driver.find_element(By.ID,
        "course-v1:Codio+python1.1+1T2025"
    )
    assert advance_button.is_displayed(), "Advance Your Career (enroll now) button is not visible"
    search_title = driver.find_element(By.CSS_SELECTOR, "h1").text
    assert "Python Programming" in search_title, (
        f"Title does not contain 'Python Programming'. "
        f"Course Title is: {search_title}"
    )

    print(
        "Advance Your Career Button is visible and the search query "
        "('Python Programming') matches the course title "
        f"('{search_title}')"
    )
except Exception as e:
    print(f"Error while testing: {e}")
finally:
    print("Driver quitting.")
    driver.quit()
