from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, AdvertisementPageLocators
from config import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD, BASE_URL
from utils import scroll_to, find_my_ad


class TestAdvertisement:

    def test_create_ad_unauthorized(self, driver, wait):

        wait.until(EC.element_to_be_clickable(MainPageLocators.PLACE_AD_BUTTON)).click()

        modal = wait.until(EC.visibility_of_element_located(AdvertisementPageLocators.MODAL_TITLE))
        assert modal.text == "Чтобы разместить объявление, авторизуйтесь"

    def test_create_ad_authorized(self, driver, wait):

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_AND_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(EXISTING_USER_EMAIL)
        
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        user_name = wait.until(EC.visibility_of_element_located(MainPageLocators.USER_NAME))
        avatar = wait.until(EC.presence_of_element_located(MainPageLocators.USER_AVATAR))
        driver.execute_script("arguments[0].click();", avatar)

        wait.until(EC.element_to_be_clickable(MainPageLocators.PLACE_AD_BUTTON)).click()
         
        scroll_to(driver, AdvertisementPageLocators.NAME_INPUT).send_keys("Объявление")

        desc = driver.find_element(*AdvertisementPageLocators.DESCRIPTION_INPUT)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", desc)
        desc.click()
        desc.send_keys("такое-то такое-то")

        scroll_to(driver, AdvertisementPageLocators.PRICE_INPUT).send_keys("1001")
        scroll_to(driver, AdvertisementPageLocators.CATEGORY_DROPDOWN).click()
        driver.find_element(By.XPATH, "//button[.//span[text()='Авто']]").click()

        scroll_to(driver, AdvertisementPageLocators.CITY_DROPDOWN).click()
        driver.find_element(By.XPATH, "//button[.//span[text()='Москва']]").click()
        element = driver.find_element(*AdvertisementPageLocators.CONDITION_RADIO_NEW)
        driver.execute_script("arguments[0].click();", element)

        driver.find_element(*AdvertisementPageLocators.PUBLISH_BUTTON).click()
        driver.get(f"{BASE_URL}/profile")
        wait.until(EC.url_contains("/profile"))

        my_ad = find_my_ad(driver, title="Объявление")
        assert my_ad.is_displayed()

        assert my_ad.is_displayed()