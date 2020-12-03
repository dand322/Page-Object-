from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_product_page(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"

    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def add_to_basket_alert(self):
        assert self.is_element_present(*ProductPageLocators.ADD_ALERT), "Add to basket alert is not presented"
        msg = self.browser.find_element(*ProductPageLocators.ADD_ALERT).text
        assert "has been added to your basket" in msg

