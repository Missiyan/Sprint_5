from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators
from config import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


class TestLogout:

    def test_logout_user(self, driver, wait):

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_AND_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGOUT_BUTTON)).click()

        login_button = wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_AND_REGISTER_BUTTON))
        assert login_button.is_displayed()