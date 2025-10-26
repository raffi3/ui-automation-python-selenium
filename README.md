
# UI Automation for Twitch
This is a Python-based UI test automation framework for Twitch.
It uses `pytest` and `selenium`.




### Benefits
#### Test stability 
- To ensure test stability all pages are waiting navigation and page content load completion, methods are using explicit waits and hard sleeps are avoided
- Streamer page pop-up is handled by setting property in browser local storage
- Network call polling interceptor is used to wait video content load
#### Structural
- The test is designed to work not only on web mobile emulator, but with perspective to work on desktop version as well (after minimal additions), since in real life scenario the test should be capable to support both versions
- The navigation component — along with its embedded search bar — has been implemented as a reusable component since it appears on multiple pages.

![UI-twitch-streamer-test-2](https://github.com/user-attachments/assets/98a332c6-b2e1-4720-a4e4-7fbf6bd6b0a1)




### Result
<img width="320" height="568" alt="streamer_page_view" src="https://github.com/user-attachments/assets/776f60d2-63f7-4320-9226-afe1c05a331e" />


### Setup

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

<img width="1152" height="642" alt="UI Allure result 2" src="https://github.com/user-attachments/assets/7056aedd-2de9-44ba-82f2-a3382c190a40" />


### Project structure
```text
ui-automation-python-selenium/
├── base/                   # Core framework logic
│   ├── __init__.py
│   └── base_page.py        # Parent class for all Page Objects. Contains base methods
│                           # like _click, _type, and explicit waits.
│
├── components/             # Reusable UI modules (parts of a page)
│   ├── __init__.py
│   ├── navigation_component.py # POM for the main navigation bar
│   └── search_component.py     # POM for the search bar logic
│
├── pages/                  # Page Object Model (POM) classes, one for each page
│   ├── __init__.py
│   ├── browse_page.py      # POM class for the "Browse" page
│   ├── home_page.py        # POM class for the main Home page
│   ├── search_results_page.py # POM class for the search results list
│   └── streamer_page.py    # POM class for an individual streamer's page
│
├── screenshots/            # Stores screenshots taken during test runs 
│
├── tests/                  # Contains all automated test scripts
│   ├── __init__.py
│   ├── conftest.py         # PyTest fixtures (e.g., driver setup, mobile emulation)
│   └── test_twitch_streamer.py # The test script for the Twitch search scenario
│
├── utils/                  # Helper modules for various tasks
│   ├── __init__.py
│   ├── browser_storage.py  # Helpers for managing localStorage/sessionStorage
│   ├── data_provider.py    # For loading and providing test data
│   ├── mobile_gestures.py  # Functions for mobile-specific actions (swipes, etc.)
│   └── waiters.py          # Custom or complex wait conditions
│
├── .gitignore              # Specifies files and folders for Git to ignore
├── config.py               # Central configuration (e.g., IS_MOBILE, URLs)
├── README.md               # Project documentation (this file)
└── requirements.txt        # List of Python dependencies (selenium, pytest, etc.)
```
