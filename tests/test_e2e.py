import time
from POM.SearchItem import SearchItem
from Utilities.BaseClass import BaseClass
from POM.CartPage import cartPage
import logging


class TestOne(BaseClass):
    """
    Navigate to Amazon homepage and search for the non-existing product from all item and then verify No results found message should be displayed or not.
    then search for existing product from all item after that select 4th item from all items.
    add product to add to cart and check price and quantity then go to cart page and increase quantity of product and
    then validate the price increase as per quantity or not.
    after validate price as per quantity remove the product from cart and verify the cart is empty or not.

    Steps Performed:
    1.Search for a non-existing product
    2.Click on search button
    3.Verify No results found message should be displayed
    4.Clear previous search item
    5.Search for an existing product
    6.Click on search button
    7.Select 4th product from list
    8.Add product to the cart
    9.Click on 4th product from list
    10.Collect all windowID
    10.Switch window to last window
    11.Click on cart page
    12.Verify the selected quantity
    13.Check the current price of product as per quantity
    14.Wait for the price to be updated and then check the price
    15.Update quantity as per requirement
    16.Remove the product from cart
    17.Verify the product remove from cart

    """

    def getLogger(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter(" %(asctime)s :%(levelname)s : %(name)s :%(message)s ")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def test_search_item(self):
        log = self.getLogger()

        log.info("Create object of class")
        items = SearchItem(self.driver)

        log.info("1.Search for a non-existing product")
        items.search_item("ld345tsxslfer")

        log.info("2.Click on search button")
        items.click_button().click()
        time.sleep(3)

        log.info("3.Verify No results found message should be displayed")
        self.search_item_verify()

        log.info("4.Clear previous search item")
        items.clear_search_bar().clear()

        log.info("5.Search for an existing product")
        items.search_item("Laptop")

        log.info("6.Click on search button")
        items.click_button().click()
        time.sleep(3)

        log.info("7.Select 4th product from list")
        self.select_fourth_item()

        log.info("8.Add product to the cart")
        items.add_item_to_cart().click()
        time.sleep(3)

        log.info("9.Click on 4th product from list")
        items.click_on_4th_product().click()
        time.sleep(3)

        log.info("10.Collect all windowID")
        window_handles = self.driver.window_handles

        log.info("10.Switch window to last window ")
        self.driver.switch_to.window(window_handles[-1])

        log.info("Create object of class")
        cart = cartPage(self.driver)

        log.info("11.Click on cart page")
        cart.click_on_cart_page().click()

        log.info("12.Verify the selected quantity")
        self.select_quantity_from_dropdown()

        log.info("13.Check the current price of product as per quantity")
        self.price_check()

        log.info("14.Wait for the price to be updated and then check the price")
        self.get_updated_price(quantity=1)

        log.info("15.Update quantity as per requirement")
        self.update_quantity(2)

        log.info("16.Remove the product from cart")
        cart.delete_product().click()

        log.info("17.Verify the product remove from cart")
        self.remove_product()




