from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageScooter:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def switch_to_window(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(url))

    def scroll_to_element(self, elment):
        elem = self.driver.find_element(*elment)
        return self.driver.execute_script("arguments[0].scrollIntoView();", elem)

    def get_current_url(self):
        return self.driver.current_url
