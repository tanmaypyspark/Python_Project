import logging
import json
import os
from webScrapping import *
from Modules_check import *
import sys
import shutil
from datetime import datetime
sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
os.path.dirname(os.path.abspath(__file__))

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
        logger.exception(f"Error: File not found at {filepath}")
        return None
    except json.JSONDecodeError:
        logger.exception(f"Error: Invalid JSON format in {filepath}")
        return None
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
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
                        logger.warn(f"Invalid line in config file: {line}")
    except FileNotFoundError:
        logger.error(f"Config file '{filename}' not found.")
    return config_data

def move_File_To_Analysis_Dir(basepath, analysis_path):
    ''' This Function is use to move the file from output to Analysis Directory'''
    for dir in os.listdir(basepath):
        # Initialize variables to track the latest file
        latest_file = None
        latest_time = 0
        for file in os.listdir(os.path.join(basepath, dir)):
            # print(file)
            file_path = os.path.join(basepath, dir, file)
            # Get the last modification time of the file
            timestamp = os.path.getmtime(file_path)
            # Update the latest file if this file is newer
            if timestamp > latest_time:
                latest_time = timestamp
                latest_file = file
            
        if latest_file:
            readable_time = datetime.fromtimestamp(latest_time).strftime('%Y-%m-%d %H:%M:%S')
            # Ensure the analysis directory exists
            os.makedirs(analysis_path, exist_ok=True)
            # Move the file
            shutil.copy(os.path.join(basepath, dir, file), analysis_path)
            logger.info(f"Copy {latest_file} to {analysis_path}")
        else:
            logger.warning(f"No files found in directory: {os.path.join(basepath, dir)}")


def delete_folder(folder_path):
    """
    Deletes the specified folder and all its contents.

    Args:
        folder_path: The path to the folder to delete.
    """
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            logger.info(f"Deleted folder: {folder_path}")
        except Exception as e:
            logger.error(f"Error deleting folder {folder_path}: {e}")
    else:
        logger.warning(f"Folder does not exist: {folder_path}")


if __name__ == "__main__":
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
    
    logger.info(f'Request Raise By:{(os.getlogin()).capitalize()}')
    # logger.info(f"Request Raised for the following stocks: {param}")
    driver_loc = bytes.fromhex(setting_Param["DRIVER_LOCATION"]).decode('utf-8')
    logger.info(driver_loc)
    ## User Details
    user_details = getUser_Input(config['UserInput'])
    for stock_name, url in user_details.items():
        logger.info(f"Request Raised for the following stocks: {stock_name}")
        sitenam = url.split('/')[2] 
        if 'moneycontrol' in sitenam:
            param = config["MoneyControl"]
            # Site Config
            element_selector = param["element_selector"]
            ts_selector = param["ts_selector"] 
            author_selector = param["author_selector"]
            # Calling the class
            MC_Obj = Moneycontrolscraper(browserObj, url, element_selector, ts_selector, author_selector)
            MC_Obj.save_Comments(stock_name)
        else:
            logger.error(f"Error: Unsupported site '{sitenam}'")
    
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
    # Move the file to the Analysis Directory
    try:
        basePath = os.getcwd()
        webpath = os.path.join(basePath, config["output_path"])
        Stagging_path = os.path.join(basePath, config["Stagging_path"])
        move_File_To_Analysis_Dir(webpath, Stagging_path)
    except Exception as e:
        logger.error(f"{str(e)}")
    logger.info("Process Completed......")
    logger.info("*"*50)
    logger.info("TASK 1 has been completed successfully")
    logger.info("*"*50)
    
    # Sentiment Analysis Start
    from sentimentAnalysis.sentimentGraph import *
    logger.info("*"*50)
    logger.info("Sentiment Analysis Started")
    logger.info("*"*50)
    try:
        finalPath = os.path.join(basePath, config["analysis_path"])
        kickOffTheSentimentAnalysis(Stagging_path, finalPath)
    except Exception as e:
        logger.error(f"{str(e)}")
    
    logger.info("Process Completed......")
    # Delete Stagging Folder
    delete_folder(Stagging_path)
    logger.info("*"*50)
    logger.info(""*10, "TASK 2 has been completed successfully", "*"*10)
    logger.info("*"*50)
    logger.info("*"*10,"THE END","*"*10)
    logger.info("press any key to exit")
    
    
    
    