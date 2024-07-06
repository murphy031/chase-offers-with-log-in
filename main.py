from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import os
import configparser
import sys

# Function to set up Chrome options for a desktop environment and user profile
def setup_desktop_driver_with_profile(profile_path, chromedriver_path):
    chrome_options = Options()
    
    # Add the user profile directory to Chrome options
    chrome_options.add_argument(f"user-data-dir={profile_path}")

    # Create a Service object with the absolute path
    service = Service(chromedriver_path)

    # Initialize the Chrome driver with these options and service
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver

# Function to read content of index.js file
def read_js_file(file_path):
    with open(file_path, "r") as file:
        js_content = file.read()
    return js_content

# Read the configuration file
config = configparser.ConfigParser()
config.read('info.config')

# Extract configuration values
chrome_driver_path = config['selenium']['chrome_driver_path']
profile_path = config['selenium']['profile_path']
username = config['selenium']['username']
password = config['selenium']['password']
url = config['selenium']['url']
frame_name = config['selenium']['frame_name']
username_field_id = config['selenium']['username_field_id']
password_field_id = config['selenium']['password_field_id']
signin_button_id = config['selenium']['signin_button_id']
div_element_id = config['selenium']['div_element_id']
index_js_path = config['selenium']['index_js_path']

# Example usage
if __name__ == "__main__":
    # Set up the driver with the user profile
    driver = setup_desktop_driver_with_profile(profile_path, chrome_driver_path)

    try:
        # Navigate to the desired website
        driver.get(url)
        
        # Switch to the frame named in the configuration because of dynamically loaded javascript frame content.
        driver.switch_to.frame(frame_name)
        
        username_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, username_field_id))
        )
    
        # Enter username
        username_box.clear()
        username_box.send_keys(username)
        print(f"Entered the name '{username}' into the username field.")

        password_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, password_field_id))
        )
        
        # Enter password
        password_box.clear()
        password_box.send_keys(password)
        print(f"Entered the password into the password field.")

        # Locate and click the sign-in button
        signin_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, signin_button_id))
        )
        signin_button.click()
        print("Logged in successfully.")

        # Switch back to the default content (main HTML document)
        driver.switch_to.default_content()

        try:
            # Wait for the div element to be clickable
            div_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, div_element_id))
            )
            div_element.click()
            print("Clicked on the div element successfully.")
        except:
            print("You must verify device. You can do this by manually clicking on the window and verifying through text message code. After verifying please rerun this script.")
            # This is to allow time for a text message to be sent and to verify device. Adjust as needed. Default is 3 minutes.
            time.sleep(180)
            print("Exiting script after 180 seconds of waiting.")
            driver.quit()
            sys.exit()
        
        try:
            # Read the index.js file
            js_file_path = os.path.join(os.path.dirname(__file__), index_js_path)
            js_script = read_js_file(js_file_path)
            driver.execute_script(js_script)
            print("Getting them cash back offers baby!")
            # Sleep for 3 minutes while the javascript runs through and clicks all of the offers. Adjust as needed for more time for script to run.
            time.sleep(180)
            print("Executed the script from index.js!")
        except Exception as e:
            print("An error occurred:", str(e))

    except Exception as e:
        print("An error occurred:", str(e))

    driver.quit()
