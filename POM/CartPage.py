from selenium.webdriver.common.by import By

class cartPage:

    def __init__(self,driver):
        self.driver = driver

    cart = (By.XPATH,"//span[@id='nav-cart-count']")
    del_item = (By.XPATH,"//input[@type='submit']")

    def click_on_cart_page(self):
        self.driver.execute_script("window.scrollTo(0,500);")
        return self.driver.find_element(*cartPage.cart)

    def delete_product(self):
        return self.driver.find_element(*cartPage.del_item)



