# Proxy-Based Request Sender

This Python script is designed for sending HTTP POST requests through a list of proxies. It utilizes threading to concurrently handle multiple requests, improving efficiency and speed. The script relies on the `requests`, `threading`, and `colorama` libraries for HTTP communication, concurrent execution, and console colorization, respectively. A custom module, `variscrapeMOD`, is used to fetch proxies.

## Features

- **Proxy Scraping:** Automatically scrapes proxies to use for sending requests.
- **Concurrent Requests:** Leverages threading to send multiple requests simultaneously.
- **Success/Fail Tracking:** Keeps track of successful and failed requests, calculating a success ratio.
- **Color-Coded Output:** Utilizes Colorama to provide color-coded console output for better readability.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `requests`
- `colorama`

You can install the required libraries using pip:

```sh
pip install requests colorama
```

## Usage

1. **Module Preparation:** Ensure the `variscrapeMOD` module is correctly set up and accessible. This module should contain a function `get_all_proxies()` that returns a list of proxies.

2. **Configuration:** Modify the script to include your desired `username`, `question`, and `deviceId` in the `send` function payload.

3. **Execution:** Run the script with Python. It will automatically start scraping proxies and sending requests using those proxies.

```sh
python bot.py
```

## How It Works

- The script starts by scraping proxies using `variscrapeMOD.get_all_proxies()`.
- It then enters a loop where it sends requests through each proxy.
- Success and failure counts are tracked, and the success ratio is calculated and displayed in the console.
- The console output is color-coded based on the success ratio (Red for low, Yellow for moderate, Green for high success ratio).

## Note

- This script is for educational and research purposes only. Misuse of this script may violate terms of service of the target website or legal regulations.
- Ensure you have permission to use and send requests to the target website.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
```
