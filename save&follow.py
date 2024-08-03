from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

ACCOUNT_EMAIL = "email"
ACCOUNT_PASSWORD = "password"

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_opt)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&"
           "keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

time.sleep(2)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD, Keys.ENTER)
time.sleep(2)
input("Press Enter after solving the Captcha")

job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for job in job_listings:
    job.click()
    time.sleep(2)

    save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button span")
    save_button.click()
    time.sleep(2)

    wait = WebDriverWait(driver, 10)
    try:
        follow_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".follow.artdeco-button.artdeco-button--secondary.ml5")))

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView(true);", follow_button)

        # Attempt to click the element using JavaScript
        driver.execute_script("arguments[0].click();", follow_button)
        print("Follow button clicked using JavaScript")

    except NoSuchElementException:
        print("Follow button not found")
    except ElementClickInterceptedException:
        print("Element click intercepted")

    time.sleep(2)
driver.quit()
