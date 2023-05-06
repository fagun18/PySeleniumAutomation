from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to website URL
driver.get("https://www.example.com/login")

# Wait for login page to load
wait = WebDriverWait(driver, 10)
login_form = wait.until(EC.visibility_of_element_located((By.ID, "login-form")))

# Fill in form fields
username_input = driver.find_element_by_name("username")
username_input.send_keys("myusername")

password_input = driver.find_element_by_name("password")
password_input.send_keys("mypassword")

# Submit form
submit_button = driver.find_element_by_css_selector("#login-form button[type='submit']")
submit_button.click()

# Wait for dashboard page to load
dashboard = wait.until(EC.visibility_of_element_located((By.ID, "dashboard")))

# Verify that dashboard page is visible
assert "Welcome to Your Dashboard" in dashboard.text

# Close the browser
driver.quit()
