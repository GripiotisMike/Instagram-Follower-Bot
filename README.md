# Instagram-Follower-Bot
A Selenium-based bot to automate following users on Instagram.

---

## Features
- 🔐 **Secure Login**: Logs in using credentials stored securely in environment variables.
- 🔍 **Target Followers**: Accesses the followers list of a specified Instagram account.
- ⏬ **Scroll Automation**: Automatically scrolls through the followers list to load more users.
- 🤝 **Auto Follow**: Attempts to follow all visible users on the list.

---

## Installation

1. Clone the repository

2. Install dependencies:
- Python 3.6 or higher
- Google Chrome browser
- ChromeDriver
- Libraries: selenium, python-dotenv

3. Download ChromeDriver and ensure it matches your Chrome browser version. Add the ChromeDriver path to your system's PATH.
 
4. Modify the .env file to match your credentials

---

## Usage 
1. Run the bot : python main.py
2. Watch as the bot logs in to Instagram, navigates to the target account's followers list, and begins following users

---

## Notes 

- Account Safety: Use this bot responsibly. Excessive following may result in your account being flagged or banned.
- Environment Variables: Always store sensitive information in .env files for security.
- Adjustments: Modify the time.sleep() intervals in the script to avoid detection.
