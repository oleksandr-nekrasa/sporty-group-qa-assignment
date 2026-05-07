from pages.bet_page import BetPage


def test_user_can_place_single_bet_successfully(driver):
    """
    Verifies the most critical user journey:
    selecting odds, entering a valid stake,
    placing a single bet, and displaying the success receipt.

    Console logs were intentionally added to improve test execution readability
    during manual review of the assignment.
    """

    print("\n[STEP] Opening application...")

    bet_page = BetPage(driver)
    bet_page.open()

    print("[STEP] Selecting betting odds...")
    bet_page.select_first_match_and_odds()

    print("[STEP] Entering stake amount...")
    bet_page.enter_stake("1")

    print("[STEP] Submitting bet...")
    bet_page.place_bet()

    print("[STEP] Verifying success receipt...")

    assert bet_page.is_success_modal_displayed()

    page_text = bet_page.get_page_text()

    print("[STEP] Verifying receipt contains key bet information...")

    assert "Bet Placed Successfully!" in page_text
    assert "Potential Payout" in page_text
    assert "Stake" in page_text
    assert "Odds" in page_text
    assert "Home" in page_text or "Away" in page_text

    print("[SUCCESS] Bet placement completed successfully.")
