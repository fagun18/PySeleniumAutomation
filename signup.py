from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to website URL
driver.get("https://www.example.com/signup")

# Wait for signup page to load
wait = WebDriverWait(driver, 10)
signup_form = wait.until(EC.visibility_of_element_located((By.ID, "signup-form")))

# Fill in form fields
name_input = driver.find_element_by_name("name")
name_input.send_keys("John Doe")

email_input = driver.find_element_by_name("email")
email_input.send_keys("johndoe@example.com")

password_input = driver.find_element_by_name("password")
password_input.send_keys("mypassword")

confirm_password_input = driver.find_element_by_name("confirm_password")
confirm_password_input.send_keys("mypassword")

# Submit form
submit_button = driver.find_element_by_css_selector("#signup-form button[type='submit']")
submit_button.click()

# Wait for confirmation message to appear
confirmation_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".message.success")))

# Verify that confirmation message is visible
assert "Your account has been created" in confirmation_message.text

# Close the browser
driver.quit()
