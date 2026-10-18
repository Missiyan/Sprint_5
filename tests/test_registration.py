from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, RegistrationPageLocators
from utils import generate_email, generate_password
from config import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD


class TestRegistration:

    def test_register_new_user_success(self, driver, wait):

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_AND_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)).click()

        email = generate_email()
        password = generate_password()

        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        avatar = wait.until(EC.visibility_of_element_located(MainPageLocators.USER_AVATAR))
        user_name = wait.until(EC.visibility_of_element_located(MainPageLocators.USER_NAME))

        assert avatar.is_displayed()
        assert user_name.text == "User."

    def test_register_invalid_email(self, driver, wait):

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_AND_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)).send_keys("invalid-email")
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        error = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR_MESSAGE))
        assert error.text == "Ошибка"

    def test_register_existing_user(self, driver, wait):

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_AND_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        error = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR_MESSAGE))
        assert error.text == "Ошибка"