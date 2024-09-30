import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    """
    Step 1: Retrieve the logger instance using self.getLogger() for logging.
    Step 2: Locate the search result elements using the XPath to find all relevant span elements that contain search result titles.
    Step 3: Extract the text from each search result element and strip any surrounding whitespace.
    Step 4: Combine all the extracted texts into one string.
    Step 5: Define the expected string that should appear if the search yields no results.
    Step 6: Check if the expected string is present in the combined text of search results.
    Step 7: If the expected string is found, log that a match was found.
    Step 8: If the expected string is not found, log that no match was found, and assert False to fail the test.

    """

    def search_item_verify(self):
        log = self.getLogger()
        elements = self.driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base']")
        texts = [element.text.strip() for element in elements]
        combined_text = " ".join(texts)
        expected_string = "No results for ld345tsxslfer ."

        # Check if the expected string is part of the combined text
        if expected_string in combined_text:
            log.info(f"Match found: {combined_text}")
        else:
            log.info(f"No match found: '{combined_text}'")
            assert False, "No match found"

    """
    Step 1: Retrieve the logger instance using self.getLogger() for logging.
    Step 2: Scroll the page down by 1500 pixels to bring the search results area into view.
    Step 3: Wait for all search result elements (identified by a specific XPath for search result components) to become visible using WebDriverWait.
    Step 4: Locate the fourth product in the list (index 3 because lists are zero-indexed).
    Step 5: Optionally scroll the fourth item into view using JavaScript to ensure it's visible.
    Step 6: Introduce a 5-second delay using time.sleep(5) to allow the user to view the item if needed.

    """

    def select_fourth_item(self):
        log = self.getLogger()
        self.driver.execute_script("window.scrollTo(0,1500);")
        wait = WebDriverWait(self.driver, 10)
        products = wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']")))
        fourth_ele = products[3]
        # Optionally, you can scroll the fourth item into view if necessary
        self.driver.execute_script("arguments[0].scrollIntoView();", fourth_ele)
        time.sleep(5)

    """
    Step 1: Retrieve the logger instance using self.getLogger() for logging.
    Step 2: Wait for the dropdown element to become visible using WebDriverWait.
    Step 3: Create a Select object for the dropdown element.
    Step 4: Use select.select_by_value() to choose the desired quantity, which is passed as an argument.
    Step 5: Log the selected quantity.
    Step 6: Introduce a 2-second delay using to allow the page to update.
    """

    def select_quantity_from_dropdown(self, desired_quantity=1):
        log = self.getLogger()
        wait = WebDriverWait(self.driver, 10)
        quantity_dropdown = wait.until(EC.visibility_of_element_located((By.ID, "quantity")))
        select = Select(quantity_dropdown)
        select.select_by_value(str(desired_quantity))
        log.info(f"Selected quantity: {desired_quantity}")
        time.sleep(2)

    """
    Step 1: Retrieve the logger instance using self.getLogger() for logging.
    Step 2: Wait for the price element (identified by an XPath locator) to become visible using WebDriverWait.
    Step 3: Extract the text of the price element.
    Step 4: Remove any commas from the price string to handle large numbers (e.g., 1,000 becomes 1000).
    Step 5: Convert the price string to a float for calculation purposes.
    Step 6: Log the current price of the product.
    Step 7: Return the price so it can be used in other methods.
    """

    def price_check(self):
        log = self.getLogger()
        wait = WebDriverWait(self.driver, 10)
        price_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))
        )
        product_price = price_element.text.replace(",", "")  # Remove any commas
        product_price = float(product_price)  # Convert price to a float for calculation
        log.info(f"Price of the product: {product_price}")
        return product_price

    """
    Step 1: Call the update_quantity() function to change the quantity of the product on the page.
    Step 2: After the quantity is updated, call the price_check() function to retrieve the new price.
    Step 3: Log the updated price for the selected quantity.
    Step 4: Return the updated price so it can be used for further calculations or assertions.
    """

    def get_updated_price(self, quantity):
        self.update_quantity(quantity)
        updated_price = self.price_check()
        log = self.getLogger()
        log.info(f"Updated price for quantity {quantity}: {updated_price}")
        return updated_price

    """
    Step 1: Retrieve the logger instance using self.getLogger() for logging.
    Step 2: Log the action of updating the quantity.
    Step 3: Wait for the quantity dropdown element (identified by the name attribute "quantity") to become visible using WebDriverWait.
    Step 4: Create a Select object for the dropdown element.
    Step 5: Use select.select_by_value() to select the new quantity.
    Step 6: Introduce a 2-second delay using time.sleep(2) to allow the page to reflect the updated quantity.
    """

    def update_quantity(self, quantity):
        log = self.getLogger()
        log.info(f"Updating quantity to {quantity}")
        quantity_dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "quantity"))
        )
        select = Select(quantity_dropdown)
        select.select_by_value(str(quantity))
        time.sleep(2)

    """
    Step 1: Retrieve the logger instance using self.getLogger() for logging.
    Step 2: Wait for the "Remove" button to be visible using WebDriverWait.
    Step 3: Check if the "Remove" button is displayed on the page.
    Step 4: If the "Remove" button is displayed, log that the product was successfully removed and the cart is empty.
    Step 5: If the "Remove" button is not displayed, log that the product was not removed or the cart is not empty.
    """

    def remove_product(self):
        log = self.getLogger()
        wait = WebDriverWait(self.driver, 10)
        empty_cart_message = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='submit']"))
        )

        if empty_cart_message.is_displayed():
            log.info(f"The product was successfully removed, and the cart is empty.")
        else:
            log.info(f"Failed to remove the product or the cart is not empty.")
