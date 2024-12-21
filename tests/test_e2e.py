import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

                # Corrected find_element usage
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        confirmpage = checkoutpage.checkOutItems()
        log.info("Entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text

        log.info("Text received from application is " + textMatch)

        assert "Success! Thank you!" in textMatch

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pageObjects.CheckoutPage import CheckOutPage
# from pageObjects.HomePage import HomePage
# from utilities.BaseClass import BaseClass
#
#
# class TestOne(BaseClass):
#
#     def test_e2e(self):
#         log = self.getLogger()
#         homePage = HomePage(self.driver)
#         checkoutpage = homePage.shopItems()
#         log.info("Getting all the card titles")
#
#         # Get card titles and iterate over them
#         cards = checkoutpage.getCardTitles()
#         for i, card in enumerate(cards):
#             # Refresh card reference to avoid stale elements
#             cardText = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of(card)
#             ).text
#             log.info(cardText)
#
#             if cardText == "Blackberry":
#                 checkoutpage.getCardFooter()[i].click()
#                 break  # Exit loop after clicking the desired card
#
#         # Proceed with checkout
#         WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class*='btn-primary']"))
#         ).click()
#
#         confirmpage = checkoutpage.checkOutItems()
#         log.info("Entering country name as 'ind'")
#         self.driver.find_element(By.ID, "country").send_keys("ind")
#
#         # Wait for and click "India"
#         WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable((By.LINK_TEXT, "India"))
#         ).click()
#
#         self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
#         self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
#
#         # Wait for and verify success message
#         textMatch = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='alert-success']"))
#         ).text
#         log.info("Text received from application is: " + textMatch)
#
#         assert "Success! Thank you!" in textMatch
