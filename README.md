# Chase Offers Automation
Automatically add all Chase credit/debit card offers from the website without having to click one-by-one.

# Selenium WebDriver Automation Script

This project provides a Selenium WebDriver script to automate interactions with Chase The script logs into the website and executes JavaScript from a provided file, based on user-defined configuration settings.

## Prerequisites

Before running the script, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (preferably Python 3)
- [Selenium WebDriver](https://pypi.org/project/selenium/) Python package
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) compatible with your Chrome browser version

## Installation

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

### 2. Install dependencies

```bash
git clone https://github.com/murphy031/chase-offers-with-log-in.git
```

### 3. Download ChromeDriver

   - Download the appropriate version of ChromeDriver for your operating system from the ChromeDriver download page. Place the chromedriver executable in a known location on your system. (chromedriver.exe)

### 4. Update the Configuration File

   - Replace your_user_profile_here with the path to your user profile directory.
   - Replace your_chase_username_here and your_chase_password_here with your Chase login credentials.
   - Ensure the index_js_path points to the location of your index.js file in the project directory.

## Running the script

### Things to know
   - When the script is first run you might have a verify device window pop up. The script will sleep for 3 minutes (adjust as needed). You will be prompted to verify device via text message code. Once you enter the code manually you can wait on the script to finish, or you can kill the script. You will then rerun the script.

### 1. Navigate to the Project Directory

   - Open a terminal or command prompt and change to the project directory:

### 2. Execute the Script

Run the script using Python:
   - ex: python main.py

## Credits

The JavaScript file `index.js` used in this project was authored by [loosiegoosey](https://github.com/loosiegoosey). It is used to [auto click the chase offers].


### MIT License

Copyright (c) [2024] [Austin Murphy]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
