# Selenium Test Automation - E-commerce Demo Store (Python)

End-to-end UI tests written in Python with Selenium WebDriver against the WooCommerce demo store at http://demostore.supersqa.com.

## Test scenarios

| Script | What it checks |
| --- | --- |
| `verify_new_user_registration.py` | Registers a new user with a randomly generated email and strong password, then asserts the user is logged in (logout link visible). |
| `login_with_invalid_user.py` | Logs in with an unregistered email and asserts the exact error message. Steps are methods of one class, in a page-object style. |
| `verify_free_coupon_works.py` | Adds an item to the cart, applies coupon SSQA100 and asserts the cart total becomes $0.00, using explicit waits. |

## Tech

Python 3, Selenium 4 (WebDriver, WebDriverWait, expected_conditions), Google Chrome.

## How to run

```bash
pip install -r requirements.txt
python verify_new_user_registration.py
python login_with_invalid_user.py
python verify_free_coupon_works.py
```

Selenium 4.6+ downloads the matching ChromeDriver automatically, so only Chrome needs to be installed. Each script prints Pass, or raises an error when a check fails.
