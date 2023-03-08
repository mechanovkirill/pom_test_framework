from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: webdriver.Chrome, url: str):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(
            ec.visibility_of_all_elements_located(locator)
        )

    def element_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(
            ec.presence_of_element_located(locator)
        )

    def elements_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(
            ec.presence_of_all_elements_located(locator)
        )

    def element_is_not_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(
            ec.invisibility_of_element_located(locator)
        )

    def element_is_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(
            ec.element_to_be_clickable(locator)
        )

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


