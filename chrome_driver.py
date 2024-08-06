from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import globalvars

try:
    # Install the ChromeDriver using webdriver-manager
    chrome_driver_path = ChromeDriverManager().install()
    
    # Print the path for debugging
    print(f"ChromeDriver Path: {chrome_driver_path}")
    
    # Manually locate the correct chromedriver.exe path
    driver_directory = os.path.dirname(chrome_driver_path)
    chrome_driver_exe = os.path.join(driver_directory, 'chromedriver.exe')
    
    # Ensure the path points to a valid .exe file
    if not os.path.isfile(chrome_driver_exe):
        raise Exception("ChromeDriver executable not found.")
    
    # Create a Service object with the correct path to the ChromeDriver
    #service = Service(chrome_driver_exe)

    # Initialize the WebDriver with the Service object
    #driver = webdriver.Chrome(service=service)

    # Update the globalvar driver
    globalvars.service = service = Service(chrome_driver_exe)


except Exception as e:
    print(f"An error occurred: {e}")