from selenium.webdriver.common.by import By


class SearchItem:
    def __init__(self,driver):
        self.driver = driver

    item = (By.XPATH,"//input[@id='twotabsearchtextbox']")
    search_click = (By.XPATH,"//input[@id='nav-search-submit-button']")
    search_bar = (By.XPATH,"//input[@id='twotabsearchtextbox']")
    add_to_cart = (By.XPATH, "//button[@id='a-autoid-3-announce']")
    product = (By.XPATH, "//div[@class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_4']//div[@class='s-product-image-container aok-relative s-text-center s-image-overlay-grey puis-image-overlay-grey s-padding-left-small s-padding-right-small puis-flex-expand-height puis puis-v2fl5pkubaqu126k6zseo6li6q']")


    def search_item(self,item):
        return self.driver.find_element(*SearchItem.item).send_keys(item)

    def click_button(self):
        return self.driver.find_element(*SearchItem.search_click)

    def clear_search_bar(self):
        return self.driver.find_element(*SearchItem.search_bar)

    def add_item_to_cart(self):
        return self.driver.find_element(*SearchItem.add_to_cart)

    def click_on_4th_product(self):
        return self.driver.find_element(*SearchItem.product)



