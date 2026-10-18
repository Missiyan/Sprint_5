import random
import string
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import re
from locators import AdvertisementPageLocators as Ads


def generate_email():
    local_part = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{local_part}@example.com"


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def scroll_to(driver, locator):
    element = driver.find_element(*locator)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    return element
    

def _page_marker(driver):
    for e in driver.find_elements(*Ads.PAGINATION_MARKER):
        t = e.text.strip()
        if re.fullmatch(r"\d+\s+из\s+\d+", t):
            return t
    return None

#найти объявление среди всех страниц
def find_my_ad(driver, title="Объявление", max_pages=20, timeout=10):
    wait = WebDriverWait(driver, timeout)
    title_xpath = Ads.AD_CARD_TITLE_TEMPLATE.format(title)

#ожидание
    wait.until(lambda d: 
        d.find_elements(By.XPATH, title_xpath)
        or _page_marker(d) is not None
        or d.find_elements(*Ads.PAGINATION_NEXT))

    for page in range(1, max_pages + 1):
        found = driver.find_elements(By.XPATH, title_xpath)
        if found:
            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", found[0])
            return found[0]

        arrows = driver.find_elements(*Ads.PAGINATION_NEXT)
        if not arrows:
            break
        arrow = arrows[-1]

        before = _page_marker(driver)

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});"
            "arguments[0].click();", arrow)

        try:
            wait.until(lambda d: _page_marker(d) != before)
        except TimeoutException:
            break

    raise AssertionError(
        f"'{title}' не найдено за {page} стр. (маркер: {_page_marker(driver)})")