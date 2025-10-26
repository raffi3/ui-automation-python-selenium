# UI Automation for Twitch
This is a Python-based UI test automation framework for Twitch.
It uses `pytest` and `selenium`.




## Benefits
#### Test stability 
To ensure test stability all pages are waiting navigation and page content load completion, methods are using explicit waits, hard sleeps are avoided
Streamer page pop-up is handled by setting property in browser local storage

![UI-twitch-streamer-test](https://github.com/user-attachments/assets/1a8c6b43-13bc-452f-b25c-1e837f6475b0)


## Result
<img width="640" height="1136" alt="streamer_page_view" src="https://github.com/user-attachments/assets/90ebf1ef-f80b-44a1-8967-0073f2c4fd85" />


## Setup

1.  **Clone the repository**
2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

# Test Run

### Standard Pytest Run

From the root directory, run:

```bash
pytest .
```

### Allure Reporting

This framework is configured to generate Allure reports.

1.  **Run tests & Generate Allure data:**
    ```bash
    pytest --alluredir=allure-results
    ```
    (This runs all tests and saves the results to the `allure-results` folder, clearing old results first)

2.  **Serve the Allure Report:**
    Once the tests are finished, run:
    ```bash
    allure serve allure-results
    ```
    This will open the interactive Allure report in your web browser.
