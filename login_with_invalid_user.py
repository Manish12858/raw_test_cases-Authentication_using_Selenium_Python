from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class InvalidUserLoginError:
    se=Service()
    invalid_email="man@gmail.com"
    url="http://demostore.supersqa.com/my-account/"
    expected_msg="ERROR: Invalid email address. Lost your password"
    def __init__(self):
        self.driver=webdriver.Chrome(service=self.se)
        self.driver.implicitly_wait(10)

    def go_to_my_account(self):
        self.driver.get(self.url)

    def input_email(self):
        field=self.driver.find_element(By.ID,'username')
        field.send_keys(InvalidUserLoginError.invalid_email)
        time.sleep(3)

    def input_password(self):
        field=self.driver.find_element(By.ID,'password')
        field.send_keys("manish@mk123")

    def click_login(self):
        self.driver.find_element(By.NAME,'login').click()

    def verify_error_message(self):
        err_elm=self.driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/ul/li')
        displayed_err=err_elm.text
        assert displayed_err==self.expected_msg, "The displayed error is not expected"
        print("pass")
    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        time.sleep(3)
        self.click_login()
        self.verify_error_message()
        self.driver.quit()

if __name__=="__main__":
    obj=InvalidUserLoginError()
    obj.main()
        