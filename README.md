# UI Automation for Twitch
This is a Python-based UI test automation framework for Twitch.
It uses `pytest` and `selenium`.

## Benefits
#### Test stability 
To ensure test stability all pages are waiting navigation and page content load completion, methods are using explict waits, hard sleeps are avoided

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
