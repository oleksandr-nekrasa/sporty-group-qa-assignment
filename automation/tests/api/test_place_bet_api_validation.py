import requests

from utils.config import BASE_URL, API_HEADERS


def test_place_bet_rejects_stake_above_maximum():
    """
    Verifies that the API rejects stake values above the allowed maximum limit.

    This test was selected because financial validation is a high-risk business area
    and is more stable and efficient to validate directly on the API layer.
    """

    print("\n[STEP] Preparing invalid bet payload...")

    payload = {
        "matchId": "premier-league-manutd-chelsea",
        "selection": "HOME",
        "stake": 100.01
    }

    print("[STEP] Sending POST request to /api/place-bet...")

    response = requests.post(
        f"{BASE_URL}/api/place-bet",
        json=payload,
        headers=API_HEADERS
    )

    print("[STEP] Verifying response status code...")

    assert response.status_code == 422

    print("[STEP] Verifying validation error response...")

    response_body = response.json()

    assert "message" in response_body

    print("[SUCCESS] API correctly rejected stake above maximum limit.")
