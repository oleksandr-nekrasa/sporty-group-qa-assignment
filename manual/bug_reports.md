# Execution Results & Bug Reports

## Executed Scenarios
The following highest-priority scenarios from the test plan were executed:

1. Scenario 1: Successful Single Bet Placement with Receipt and Balance Update
2. Scenario 2: Stake Validation Boundaries and Input Format
3. Scenario 3: Selection Replacement in Bet Slip

Additional exploratory checks were performed around the bet placement flow, receipt modal, balance update, stake input robustness, date filters, and API response consistency.

# BUG-001: Incorrect Potential Payout Displayed in Success Receipt Modal

**Severity:** High  
**Priority:** High  
**Area:** Payout Calculation

## Environment
- Application URL: https://qae-assignment-tau.vercel.app/?user-id=candidate-x5Jr7NwP1U
- Browser: Google Chrome Version 147.0.7727.56  (Official Build) (64-bit)
- User ID: candidate-x5Jr7NwP1U

## Frequency
Reproducible: 3/3

## Description
The Potential Payout value displayed in the success receipt modal is incorrectly calculated after successful bet placement.

## Preconditions
- User is logged in with a valid user ID
- Available balance is sufficient

## Steps to Reproduce
1. Navigate to the Upcoming Football Matches page.
2. Select any football match.
3. Select odds with a specific value, e.g. `3.25`.
4. Enter a stake amount, e.g. `€40.00`.
5. Click **Place Bet**.
6. Wait for the success receipt modal.
7. Observe the displayed Potential Payout value.

## Expected Result
Potential payout is correctly calculated and displayed:
Stake × Odds
€40.00 × 3.25 = €130.00

The receipt should display:

Potential Payout: €130.00

## Actual Result
The success receipt modal displays mathematically incorrect potential payout value: 

Potential Payout: €80.00

## Business Impact
Incorrect payout calculation may:
- reduce user trust in the betting platform,
- create confusion regarding expected winnings,
- lead to disputes related to payout correctness,
- negatively affect the credibility of the bet placement flow.

## Evidence 
- manual/screenshots/bug-001-incorrect-payout.png

## Technical Notes
A quick Network check showed that `POST /api/place-bet` returns a successful `200 OK` response. Further investigation should compare the API response and receipt rendering for the exact same stake/odds combination to confirm whether the issue is caused by backend calculation or frontend receipt mapping.

## Additional Observation
During API inspection, the `POST /api/place-bet` response returned:

{
  "currency": "USD"
}
while the specification and UI examples reference EUR (€) values.

This may indicate environment/mock-data inconsistency, backend currency configuration issue, or mismatch between API and UI expectations.

# BUG-002: Selected Betting Outcome Is Missing from Success Receipt Modal

**Severity:** High 
**Priority:** High 
**Area:** Bet Receipt / Selection Details

## Environment
- Application URL: https://qae-assignment-tau.vercel.app/?user-id=candidate-x5Jr7NwP1U
- Browser: Google Chrome Version 147.0.7727.56 (Official Build) (64-bit)
- User ID: candidate-x5Jr7NwP1U

## Frequency
Reproducible: 3/3

## Description
The success receipt modal does not display the selected betting outcome after successful bet placement. Users cannot verify which outcome was actually placed.

## Preconditions
- User is logged in with a valid user ID
- Available balance is sufficient

## Steps to Reproduce
1. Navigate to the Upcoming Football Matches page.
2. Select any football match.
3. Select a specific betting outcome, e.g. `Match Winner: Away`.
4. Enter a valid stake amount.
5. Click **Place Bet**.
6. Wait for the success receipt modal.
7. Observe the displayed receipt details.

## Expected Result
The success receipt modal should clearly display:
- selected outcome
Example:
Selection: Away

## Actual Result
The success receipt modal displays:
- match details,
- stake amount,
- odds value,
- potential payout,
but does not display the selected betting outcome.

## Business Impact

Missing selection information may:
- create ambiguity regarding the placed bet, 
- reduce user confidence in the transaction, 
- make bet verification difficult, 
- increase the likelihood of user disputes or support requests.

## Evidence 
- manual/screenshots/bug-002-missing-selection.png

# BUG-003: User Balance Is Not Updated After Successful Bet Placement Until Page Refresh

**Severity:** Medium
**Priority:** Medium
**Area:** Balance / UI State Management

## Environment
- Application URL: https://qae-assignment-tau.vercel.app/?user-id=candidate-x5Jr7NwP1U
- Browser: Google Chrome Version 147.0.7727.56 (Official Build) (64-bit)
- User ID: candidate-x5Jr7NwP1U

## Frequency
Reproducible: 3/3

## Description
The available user balance displayed in the top-right corner is not updated immediately after successful bet placement. The balance is refreshed only after manually reloading the page.

## Preconditions
- User is logged in with a valid user ID
- Available balance is sufficient

## Steps to Reproduce
1. Navigate to the Upcoming Football Matches page.
2. Observe the current available balance displayed in the top-right corner.
3. Select any football match.
4. Select any betting outcome.
5. Enter a valid stake amount.
6. Click **Place Bet**.
7. Wait for the success receipt modal.
8. Observe the displayed balance in the top-right corner.
9. Refresh the page.
10. Observe the balance again.

## Expected Result
The available balance should be updated immediately after successful bet placement by deducting the placed stake amount.

## Actual Result
The balance displayed in the top-right corner remains unchanged after successful bet placement.

The correct balance is displayed only after manually refreshing the page.

## Business Impact
Delayed balance updates may:
- confuse users regarding their available funds,
- create inconsistent UI state,
- reduce confidence in transaction correctness,
- lead users to believe the bet was not processed successfully.

## Evidence
Observed during live interaction. Static screenshot does not clearly represent the issue because the balance updates correctly only after manual page refresh.

# BUG-004: Stake Input Accepts Extremely Large Numbers Causing Scientific Notation and UI Overflow

**Severity:** Medium
**Priority:** Medium
**Area:** Stake Validation / Numeric Formatting

## Environment
- Application URL: https://qae-assignment-tau.vercel.app/?user-id=candidate-x5Jr7NwP1U
- Browser: Google Chrome Version 147.0.7727.56 (Official Build) (64-bit)
- User ID: candidate-x5Jr7NwP1U

## Frequency
Reproducible: 3/3

## Description
The stake input field accepts extremely large numeric values. As a result, the UI displays scientific notation values and layout overflow in the bet slip summary section.

## Preconditions
- User is logged in with a valid user ID
- Any football match and betting outcome are selected

## Steps to Reproduce
1. Navigate to the Upcoming Football Matches page.
2. Select any football match and betting outcome.
3. In the stake input field, enter an extremely large numeric value, e.g.:34234234234234234234234234
4. Observe the bet slip summary section.

## Expected Result
The application should:
- prevent excessively large numeric input,
- properly validate stake length/value,
- maintain correct UI formatting,
- avoid displaying scientific notation values in the user interface.

## Actual Result
The application accepts extremely large numeric values and displays:
- scientific notation values,
- broken currency formatting,
- UI overflow in the bet slip summary section.

Example displayed values:
Total Stake: €2.3423423423423422e+29
Potential Payout: €7.495495495495495e+29

## Business Impact
Improper handling of extremely large stake values may:
- reduce confidence in financial calculations,
- create confusing or unreadable UI states,
- expose weaknesses in frontend validation logic,
- negatively affect perceived application stability and reliability.

## Evidence
- manual/screenshots/bug-004-scientific-notation-overflow.png

# Exploratory Observations

## OBS-001: Date Filter Default State Inconsistency
The Date filter opens with the `Custom` tab visually selected while no date is actually applied. After clicking `Reset`, the filter correctly switches to `All`.

This may create ambiguity regarding the currently active filter state.

## Evidence
- manual/screenshots/obs-001-date-filter-state.png

## OBS-002: Reset Action Applies Changes Without Confirmation
Clicking `Reset` immediately updates the match list even without clicking `Apply`.

This behavior appears inconsistent with the modal confirmation flow.

## OBS-003: Single Date Formatting Inconsistency
When selecting a single date, the date value is displayed in red, while date ranges are displayed using standard text color.

This may create inconsistent visual feedback for filter states.

## OBS-004: Filtered Match List Appears Unsorted
After applying date filters, the displayed matches do not appear to be sorted chronologically.

Further clarification of expected sorting behavior may be required.

## OBS-005: Match Counter Does Not Reflect Filtered Results
After applying date filters, the header still displays:

Showing 103 matches
even though the visible filtered results contain significantly fewer matches.

## Evidence
- manual/screenshots/obs-005-incorrect-match-counter.png
