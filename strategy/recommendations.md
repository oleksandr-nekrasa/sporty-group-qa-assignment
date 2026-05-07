# Strategy & Recommendations

## Why These Tests Were Selected

### UI E2E Test — Successful Bet Placement

This scenario was selected because it represents the most critical user journey in the application:
- selecting odds,
- entering a valid stake,
- placing a bet,
- verifying successful receipt generation.

This flow validates core business functionality and provides high confidence that the primary betting flow works correctly from the user perspective.

---

### API Test — Maximum Stake Validation

This test validates one of the most important financial business rules directly on the API layer.

It was selected because:
- financial validation is a high-risk area,
- API validation is faster and more stable than UI validation,
- backend validation should not rely only on frontend restrictions.

---

## What Was Intentionally Left as Manual Testing

The following areas were intentionally left primarily for manual and exploratory testing:
- visual/UI consistency,
- filtering UX behavior,
- layout and formatting issues,
- exploratory edge cases,
- usability observations.

These areas change more frequently and benefit more from human exploratory validation than stable automation coverage.

---

## Recommendations for Scaling the Project

### 1. CI/CD Integration

Integrate automated tests into CI/CD pipelines using GitHub Actions or Jenkins to enable continuous validation on pull requests and deployments.

---

### 2. Expanded API Coverage

Add broader API contract and negative validation coverage:
- authentication scenarios,
- malformed payload validation,
- concurrency handling,
- response schema validation.

---

### 3. Test Reporting and Execution Strategy

As the automation suite grows, introduce:
- structured reporting (e.g. Allure),
- smoke and regression suites,
- parallel execution,
- centralized test data management.

## Notes 
Current implementation uses a static test user for simplicity.
In production-grade automation, test data isolation and state reset mechanisms should be introduced.