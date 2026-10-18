from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators
from config import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


class TestLogin:

    def test_login_existing_user(self, driver. wait):

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_AND_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        avatar = wait.until(EC.visibility_of_element_located(MainPageLocators.USER_AVATAR))
        user_name = wait.until(EC.visibility_of_element_located(MainPageLocators.USER_NAME))

        assert avatar.is_displayed()
        assert user_name.text == "User."