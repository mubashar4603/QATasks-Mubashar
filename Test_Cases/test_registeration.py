from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.randomData import randomy



class Test_01_regiteration():
    url = "https://staging.metutors.com/signup"
    firstName = 'Test'
    lastName = 'teacher'
    email = "test@gmail.com"

    def test_register(self):
        # launch the browser
        driver = webdriver.Chrome()
        # maximize the windows
        driver.maximize_window()
        # navigate to url
        driver.get(self.url)
        time.sleep(2)
        # start the test case script
        driver.find_element(By.CSS_SELECTOR,
                            'button[class="mat-focus-indicator mat-button mat-button-base ng-star-inserted"]').click()
        time.sleep(1)
        driver.find_element(By.ID, 'firstName').send_keys(self.firstName)
        driver.find_element(By.ID, 'lastName').send_keys(self.lastName)
        time.sleep(1)
        driver.find_element(By.ID, 'email').send_keys(randomy.add_random_numbers_to_email(self.email))
        time.sleep(1)
        driver.find_element(By.ID, 'phone').send_keys(randomy.generate_random_phone_number())
        time.sleep(1)
        driver.find_element(By.ID, 'pass').send_keys('Metutors@123')
        driver.find_element(By.ID, 'pass2').send_keys('Metutors@123')
        time.sleep(1)
        driver.execute_script('window.scrollBy(0,500);')
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'span[class="mat-checkbox-inner-container"]').click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
                            'button[class="mat-focus-indicator mat-flat-button mat-button-base mat-primary d-block py-1 rounded-btn w-100"]').click()
        time.sleep(3)
        actual_title = driver.title
        print(actual_title)
        if actual_title == "Sign up - MEtutors Platform":
            assert True
            driver.close()
        else:
            driver.close()
            assert False











