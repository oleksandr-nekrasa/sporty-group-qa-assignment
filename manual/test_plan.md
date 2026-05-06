# Test Plan – Single Bet Placement

## Objective
Validate the most business-critical and risk-sensitive areas of the Single Bet Placement feature for upcoming football matches.

The test plan focuses on:
- successful single bet placement
- stake validation and boundary conditions
- selection behavior
- balance and payout correctness
- error handling and retry behavior
- filtering behavior
- key API validation risks

---

## Scenario 1: Successful Single Bet Placement with Receipt and Balance Update

**Priority:** Critical

**Risk Rationale:**  
Bet placement is the core business flow. Incorrect placement, wrong payout, or incorrect balance deduction directly affects user trust and financial correctness.

**Steps:**
1. Open the application with a valid user ID.
2. Select an upcoming football match.
3. Select one odds option, e.g. HOME / 1.
4. Enter a valid stake, e.g. €10.00.
5. Verify potential payout is calculated as stake × selected odds.
6. Click **Place Bet**.
7. Verify the button enters the **Placing...** loading state.
8. Verify the success receipt modal is displayed.
9. Verify the receipt contains:
   - Bet ID
   - Match details
   - Selection
   - Stake
   - Odds at placement
   - Potential payout
   - Placement timestamp
10. Verify the available balance is reduced by the placed stake.
11. Close the receipt.

**Expected Result:**
- Bet is placed successfully.
- Stake is deducted from the available balance.
- Receipt data is consistent with selected match, stake, odds, and calculated payout.
- Closing the receipt returns the user to the main flow without an active selection.

---

## Scenario 2: Stake Validation Boundaries and Input Format

**Priority:** Critical

**Risk Rationale:**  
Stake validation protects the user and business from invalid financial transactions. Boundary errors can cause incorrect bet placement, failed transactions, or financial inconsistencies.

**Steps:**
1. Select any valid football match and odds.
2. Verify that placing a bet without stake is blocked.
3. Enter a non-numeric value into the stake field.
4. Enter invalid input formats:
   - `10,5`
   - `10..5`
   - `10.5.1`
5. Enter a stake below the allowed minimum, e.g. €0.99.
6. Enter boundary values around the minimum, e.g. €1.00 and €1.01.
7. Enter the maximum allowed stake, €100.00.
8. Enter a stake above the maximum, e.g. €100.01.
9. Enter a stake with more than 2 decimal places, e.g. €10.999.
10. Enter a stake higher than the available balance.

**Expected Result:**
- Missing stake is blocked.
- Non-numeric values are rejected.
- Invalid input formats are rejected.
- Stakes below the minimum are rejected with message:
  `Minimum stake is €1.00`
- Valid boundary values are handled according to business rules.
- Stake above €100.00 is rejected with message:
  `Maximum stake is €100.00`
- Stake with more than 2 decimal places is rejected.
- Stake higher than available balance is rejected with message:
  `Insufficient balance`

**Note:**  
The specification contains an inconsistency: business rules mention minimum stake as €1.00, while validation rules mention minimum €1.01. This should be clarified before release.

---

## Scenario 3: Selection Replacement in Bet Slip

**Priority:** High

**Risk Rationale:**  
Only one active selection is supported. Incorrect replacement behavior may result in users placing a bet on the wrong match or outcome.

**Steps:**
1. Select odds for one match, e.g. HOME / 1.
2. Verify the selection is shown in the bet slip.
3. Select different odds from another match or another outcome.
4. Verify the previous selection is automatically replaced.
5. Enter a valid stake.
6. Verify payout is recalculated using the newly selected odds.
7. Remove the active selection using the remove (X) action.
8. Verify the bet slip becomes empty.
9. Add another selection and use the Remove All action.

**Expected Result:**
- Only one selection is active at any time.
- Selecting new odds replaces the previous selection without requiring manual removal.
- Bet slip displays the latest selected match and outcome.
- Potential payout is recalculated based on the latest selection.
- Individual remove action clears the current selection.
- Remove All clears the entire bet slip state.

---

## Scenario 4: Bet Placement Failure and Error Modal Behavior

**Priority:** High

**Risk Rationale:**  
Failed bet placement must be handled safely. Users need clear recovery options, and the system must prevent duplicate or inconsistent bet states.

**Steps:**
1. Select a valid match and odds.
2. Enter a valid stake.
3. Click **Place Bet**.
4. Verify the button enters the **Placing...** loading state.
5. Trigger or simulate a backend/API failure (e.g. network interruption or mocked server error).
6. Verify the error modal is displayed with title **Something went wrong**.
7. Verify the modal body explains that the bet could not be processed and suggests trying again.
8. Verify the flow resolves to a single final state (failure modal displayed).
9. Click **Rebet**.
10. Verify the modal closes and placement is retried.
11. Trigger another failure and click **Close**.
12. Verify the modal closes and current selection/stake are cleared.
13. Repeat and close the modal using the top-right **X**.

**Expected Result:**
- Error modal is displayed after failed placement.
- **Placing...** state is visible before the final outcome.
- **Rebet** retries placement.
- **Close** clears current selection and stake.
- Top-right **X** behaves the same as **Close**.
- No duplicate bet is created during retry.

---

## Scenario 5: Date and Odds Filter Validation

**Priority:** Medium

**Risk Rationale:**  
Filters affect match discovery. Incorrect filtering may hide valid betting opportunities or show invalid matches, directly impacting conversion and user experience.

**Steps:**
0. Verify the match list contains only upcoming football matches.
1. Apply a single-day date filter.
2. Verify only matches from the selected date are displayed.
3. Apply a date range filter.
4. Verify matches from the full inclusive range are displayed.
5. Apply valid min/max odds filter values.
6. Verify only matches with odds within the inclusive range are displayed.
7. Apply an invalid odds range, e.g. min odds greater than max odds.

**Expected Result:**
- Only upcoming football matches are displayed in the sportsbook list.
- Single-day date filter returns only matches from that date.
- Date range filter includes both start and end dates.
- Odds filter returns only matches within the selected range.
- Invalid odds range is rejected with clear feedback.

---

## Scenario 6: API Validation for Bet Placement

**Priority:** High

**Risk Rationale:**  
API validation protects the system from invalid or unauthorized requests. Since bet placement involves financial state changes, backend validation must not rely only on UI restrictions.

**Steps:**
1. Send `POST /api/place-bet` without `x-user-id` header.
2. Send request with malformed JSON payload.
3. Send request with missing `matchId`.
4. Send request with unknown `matchId`.
5. Send request with invalid selection value.
6. Send request with invalid stake, e.g. below minimum or above maximum.
7. Send unsupported HTTP method to the endpoint.
8. Attempt concurrent placement requests for the same user session.

**Expected Result:**
- Missing or invalid user context returns `401 Unauthorized`.
- Malformed payload returns `400 Bad Request`.
- Missing or unknown match ID returns `422 Unprocessable Entity`.
- Invalid selection returns `422 Unprocessable Entity`.
- Invalid stake returns `422 Unprocessable Entity`.
- Unsupported HTTP method returns `405 Method Not Allowed`.
- Concurrent placement for the same user returns `409 Conflict`.