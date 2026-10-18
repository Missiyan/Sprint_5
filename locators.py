from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_AND_REGISTER_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    PLACE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    USER_AVATAR = (By.XPATH, "//button[contains(@class,'circleSmall')]")
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

class RegistrationPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//span[normalize-space()='Ошибка']")

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

class AdvertisementPageLocators:
    MODAL_TITLE = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Название']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button")
    
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CONDITION_RADIO_NEW = (By.XPATH, "//input[@type='radio' and @value='Новый']")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")
    MY_ADS_BLOCK = (By.XPATH, "//h2[text()='Мои объявления']")
    AD_CARD_TITLE_TEMPLATE = "//*[normalize-space(text())='{}']"
    PAGINATION_NEXT = (By.CSS_SELECTOR, "button.arrowButton--right:not([disabled])")
    PAGINATION_MARKER = (By.XPATH, "//*[contains(text(), ' из ')]")