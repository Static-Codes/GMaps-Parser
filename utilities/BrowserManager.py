from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os


# Handling dynamic, cross-platform chrome binary path resolution.
BINARY_FILENAME = "CHROME_BINARY_PATH"
PATH_DATA = None

def ensure_browser_binary_is_set():
    global BINARY_FILENAME
    global PATH_DATA

    if not os.path.exists(BINARY_FILENAME):
        PATH_DATA = input("Please enter the path to your installation of Chrome: ")
        with open(BINARY_FILENAME, "w") as file:
            file.write(PATH_DATA)
        
    else:
        with open(BINARY_FILENAME, "r") as file:
            PATH_DATA = file.read()

    if not os.path.exists(PATH_DATA):
        print(f"Unable to locate Chrome at: '{PATH_DATA}'")
        exit(1)
            
class BrowserManager:

    @staticmethod
    def initialize_browser():
        ensure_browser_binary_is_set()
        options = webdriver.ChromeOptions()
        options.binary_location = PATH_DATA
        options.add_argument("--log-level=3")
        options.add_experimental_option(
            "prefs", {"download.default_directory": os.getcwd() + "/"}
        )
        try:
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()), options=options
            )
            driver.set_window_position(0, 1920)
            return driver
        except Exception as e:
            print("[INFO] There was an error while initializing browser")
            print(e)
            exit()
