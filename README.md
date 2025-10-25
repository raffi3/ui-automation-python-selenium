# UI Automation for Twitch
This is a Python-based UI test automation framework for Twitch.
It uses `pytest` and `selenium`.




## Benefits
#### Test stability 
To ensure test stability all pages are waiting navigation and page content load completion, methods are using explict waits, hard sleeps are avoided
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
