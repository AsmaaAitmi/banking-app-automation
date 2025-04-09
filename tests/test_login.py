from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_login():
    print("🚀 Starting login test...")  # Add this

    driver = webdriver.Chrome()  # This should open Chrome

    driver.get("https://demo.applitools.com")

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("password")

    driver.find_element(By.ID, "log-in").click()

    time.sleep(3)

    assert "ACME" in driver.title


    driver.quit()

    print("✅ Test finished successfully!")  # Add this too

