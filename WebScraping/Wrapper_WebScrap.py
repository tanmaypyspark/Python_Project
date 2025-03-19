import logging
import json
import os
from webScrapping import *
from Modules_check import *

# Configure the logger (do this once at the beginning of your script)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
os.getcwd()

class Parent():
    def __init__(self, driver, scroll_time, max_scroll, chrome_options, driver_location):
        Parent.DRIVER = driver
        Parent.SCROLL_PAUSE_TIME = scroll_time
        Parent.MAX_SCROLLS = max_scroll
        Parent.CHROME_OPTIONS = chrome_options
        Parent.DRIVER_LOCATION = driver_location
    
    
def getConfig(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filepath}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def getUser_Input(filename):
    """Reads a config file and returns a dictionary of stock names and URLs."""
    config_data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if line:  # Skip empty lines
                    try:
                        stock_name, url = line.split(': ', 1)  # Split at the first ': '
                        config_data[stock_name] = url
                    except ValueError:
                        print(f"Warning: Invalid line in config file: {line}")
    except FileNotFoundError:
        print(f"Error: Config file '{filename}' not found.")
    return config_data

# ******** Environment Setup ********
if preSetupCheck():
    logger.info("All modules are available.")
else:
    logger.error("Error: Required modules are not available.")
# ***********************************
config_path = r'Config\config.json'
config = getConfig(config_path)
# Setting the Broswer
setting_Param = config["settings"]
browserObj = Parent(setting_Param["DRIVER"],
                    setting_Param["SCROLL_PAUSE_TIME"],
                    setting_Param["MAX_SCROLLS"],
                    setting_Param["CHROME_OPTIONS"],
                    setting_Param["DRIVER_LOCATION"])

# if __name__ == "__main__":
#     logger.info(f'Request Raise By:{(os.getlogin()).capitalize()}')
#     # logger.info(f"Request Raised for the following stocks: {param}")
#     ## User Details
#     user_details = getUser_Input(config['UserInput'])
#     for stock_name, url in user_details.items():
#         logger.info(f"Request Raised for the following stocks: {stock_name}")
#         sitenam = url.split('/')[2] 
#         if 'moneycontrol' in sitenam:
#             param = config["MoneyControl"]
#             # Site Config
#             element_selector = param["element_selector"]
#             ts_selector = param["ts_selector"] 
#             author_selector = param["author_selector"]
#             # Calling the class
#             MC_Obj = Moneycontrolscraper(browserObj, url, element_selector, ts_selector, author_selector)
#             MC_Obj.save_Comments(stock_name)
#         else:
#             logger.error(f"Error: Unsupported site '{sitenam}'")