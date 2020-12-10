from selenium import webdriver

# First we need to create an instance of the Chrome class
browser = webdriver.Chrome()
browser.get("https://github.com")

# Next we need to click on the sign in button
# In this instance, we can only find the button by its text
signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

# Next we need to fill in the login credentials
# The login field has an id, so we'll use that
username_box = browser.find_element_by_id("login_field")
password_box = browser.find_element_by_id("password")

# Now we send the keys
username_box.send_keys("user_username")
password_box.send_keys("user_password")

password_box.submit()

# Now we need to make an assertion to make sure our bot was able to sign in
# We use the assert statement to verify something
# If the username is found the execution will continue
# Otherwise it'll throw an exception AssertionError
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "user_username" in link_label

# Quit the browser
browser.quit()
