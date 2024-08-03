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
    chrome_options.add_argument(f"user-data-dir={profile_path}")
    chrome_options.add_argument("--log-level=3")  # Suppresses most logs
    chrome_options.add_argument("--silent")       # Further reduces logs
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=chrome_options)


# Function to read the content of a JavaScript file
def read_js_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
    

def shadow_host_selector(driver, ID):
    # Access the shadow root for the password field
    shadow_host = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, ID))
    )
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
    return shadow_root


def enter_info(driver, element, entered_info):
    username_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f"#{element}"))
    )
    username_box.clear()
    username_box.send_keys(entered_info)
    print(f"Entered '{entered_info}' into {element} field.")


def click_button(driver, ID):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, ID))
    )
    button.click()
    print(f"{ID} clicked successfully")


def run_deal_selector(driver, index_js_path):
    # Execute the JavaScript file
    try:
        time.sleep(5)
        js_file_path = os.path.join(os.path.dirname(__file__), index_js_path)
        js_script = read_js_file(js_file_path)
        driver.execute_script(js_script)
        print("Executed the script from index.js!")
        time.sleep(60)
    except Exception as e:
        print("An error occurred while executing the JavaScript:", str(e))


# Function to perform the login and click process
def perform_login_and_click(driver, username, password, url, frame_name, username_field_id, password_field_id, signin_button_id, div_element_id, index_js_path):
    try:
        # Navigate to the URL
        driver.get(url)
        
        # Switch to the frame
        driver.switch_to.frame(frame_name)
        
        # Access the shadow root for the username field
        shadow_root = shadow_host_selector(driver, "userId")
        
        # Enter username
        enter_info(shadow_root, username_field_id, username)
        
        # Access the shadow root for the password field
        shadow_root2 = shadow_host_selector(driver, "password")
        
        # Enter password
        enter_info(shadow_root2, password_field_id, password)
        
        # Click the login button
        click_button(driver, signin_button_id)
        
        # Switch back to the default content and escape the iframe
        driver.switch_to.default_content()

        try:
            # Click the div element
            click_button(driver, div_element_id)
        except:
            print("You must verify the device manually. After verifying, please rerun this script.")
            time.sleep(180)
            print("Exiting script after 180 seconds of waiting.")
            driver.quit()
            sys.exit()
        
        run_deal_selector(driver, index_js_path)

    except Exception as e:
        print("An error occurred during the login process:", str(e))

def main():
    # Read configuration file
    config = configparser.ConfigParser()
    config.read('info.config')

    # Extract common configuration values
    chrome_driver_path = config['selenium']['chrome_driver_path']
    profile_path = config['selenium']['profile_path']
    url = config['selenium']['url']
    frame_name = config['selenium']['frame_name']
    username_field_id = config['selenium']['username_field_id']
    password_field_id = config['selenium']['password_field_id']
    signin_button_id = config['selenium']['signin_button_id']
    div_element_id = config['selenium']['div_element_id']
    index_js_path = config['selenium']['index_js_path']

    # Set up the driver with the user profile
    driver = setup_desktop_driver_with_profile(profile_path, chrome_driver_path)

    # Perform login and click process for each user
    for section in config.sections():
        if section.startswith('user'):
            username = config[section]['username']
            password = config[section]['password']
            print(f"Processing credentials for {username}")
            perform_login_and_click(driver, username, password, url, frame_name, username_field_id, password_field_id, signin_button_id, div_element_id, index_js_path)

    driver.quit()

if __name__ == "__main__":
    main()
