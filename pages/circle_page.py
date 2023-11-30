from selenium.webdriver.common.by import By
from pages.base_page import Page


class CirclePage(Page):
    TABS = (By.CSS_SELECTOR, "[class*='styles__PageSelectionText'] a")

    def open_circle(self):
        self.open_url("https://www.target.com/circle")

    def verify_can_click_tabs(self):
        tabs = self.find_elements(*self.TABS)
        #print(tabs)
        #self.driver.refresh()
       # print('AFTER REFRESH')
        #tabs = self.find_elements(*self.TABS)
        #print(tabs)
        current_url = ''
        for i in range(len(tabs)):
            self.find_elements(*self.TABS)[i].click()
            self.wait_for_url_to_change(current_url)
            current_url = self.driver.current_url

