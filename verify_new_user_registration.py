from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import string
import random
import time

se=Service()
driver=webdriver.Chrome()
driver.implicitly_wait(10)
time.sleep(2)

url="http://demostore.supersqa.com/my-account/"
email_field_id="reg_email"
psswd_field_id="reg_password"
logout_btn_css="#post-9 > div > div > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout"

driver.get(url)
email_field = driver.find_element('id',email_field_id)

# generate random email
letters=string.ascii_lowercase
rand_string=''.join(random.choice(letters) for i in range(15))
random_email=rand_string + "@gmail.com"

# typing in the email field
email_field.send_keys(random_email)

# finding password field and entering password
password_field=driver.find_element('id',psswd_field_id)

# Generating a strong random password
passw  =''.join(str(random.randint(0,10) for i in range(6)))
passw +=''.join(random.choice(string.ascii_letters) for i in range(5))
passw += ''.join(random.choice(('#','@','&','$','*')) for i in range(5))

# Typing strong password in password field
password_field.send_keys(passw)


# finding submit button and clicking it
time.sleep(2)
register_btn=driver.find_element('css selector','button[value="Register"]')
register_btn.click()


logout_btn=driver.find_element('css selector',logout_btn_css)


if logout_btn.is_displayed():
    print('pass')
else:
    raise Exception("User not logged in after register")
# driver.close()
