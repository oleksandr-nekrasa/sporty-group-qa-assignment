from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import FULL_URL


class BetPage:

    MATCH_CARD = (By.CSS_SELECTOR, "[id^='match-card-']")
    ODDS_BUTTON = (By.CSS_SELECTOR, "button.oddsButton[id^='odds-']")
    STAKE_INPUT = (By.ID, "bet-slip-stake-input")
    PLACE_BET_BUTTON = (By.ID, "bet-slip-place-bet")
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