from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import FULL_URL


class BetPage:

    BALANCE_HEADER = (By.XPATH, "//*[contains(text(), 'Balance:')]")
    MATCH_CARD = (By.CSS_SELECTOR, "[id^='match-card-']")
    ODDS_BUTTON = (By.CSS_SELECTOR, "button.oddsButton[id^='odds-']")
    PAYOUT_VALUE = (By.XPATH, "//*[contains(text(), 'Potential Payout')]/following::*[contains(text(), '€')]")
    PLACE_BET_BUTTON = (By.ID, "bet-slip-place-bet")
    STAKE_INPUT = (By.ID, "bet-slip-stake-input")
    SUCCESS_MODAL = (By.XPATH, "//h2[contains(text(), 'Bet Placed Successfully!')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(FULL_URL)

    def select_first_match_and_odds(self):
        self.wait.until(
            EC.presence_of_all_elements_located(self.MATCH_CARD)
        )

        odds_buttons = self.driver.find_elements(*self.ODDS_BUTTON)
        odds_buttons[0].click()

    def enter_stake(self, amount):
        stake_input = self.wait.until(
            EC.visibility_of_element_located(self.STAKE_INPUT)
        )

        stake_input.clear()
        stake_input.send_keys(str(amount))

    def place_bet(self):
        place_bet_button = self.wait.until(
            EC.element_to_be_clickable(self.PLACE_BET_BUTTON)
        )

        place_bet_button.click()

    def is_success_modal_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MODAL)
        ).is_displayed()

    def get_payout_value(self):
        payout = self.wait.until(
            EC.visibility_of_element_located(self.PAYOUT_VALUE)
        )
        return payout.text

    def get_balance_value(self):
        balance = self.wait.until(
            EC.visibility_of_element_located(self.BALANCE_HEADER)
        )
        return balance.text

    def get_bet_slip_text(self):
        return self.driver.page_source

    def get_page_text(self):
        return self.driver.find_element("tag name", "body").text
