'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''

# Imports

import os
import json
import logging
from time import sleep
from random import randint
from datetime import datetime, timedelta
from pprint import pprint

try:
    from config.settings import logs_folder_path
except ImportError:
    # Fallback if config.settings is missing
    logs_folder_path = "./logs"

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


#### Common functions ####

#< Directories related
def make_directories(paths: list[str]) -> None:
    '''
    Function to create missing directories
    '''
    for path in paths:  
        path = path.replace("//","/")
        if '/' in path and '.' in path: path = path[:path.rfind('/')]
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except Exception as e:
            logging.error(f'Error while creating directory "{path}": {e}')


def find_default_profile_directory() -> str | None:
    '''
    Function to search for Chrome Profiles within default locations
    '''
    default_locations = [
        r"%LOCALAPPDATA%\Google\Chrome\User Data",
        r"%USERPROFILE%\AppData\Local\Google\Chrome\User Data",
        r"%USERPROFILE%\Local Settings\Application Data\Google\Chrome\User Data"
    ]
    for location in default_locations:
        profile_dir = os.path.expandvars(location)
        if os.path.exists(profile_dir):
            return profile_dir
    return None
#>


#< Logging related
def critical_error_log(possible_reason: str, stack_trace: Exception) -> None:
    '''
    Function to log and print critical errors along with datetime stamp
    '''
    logging.critical(f"{possible_reason}\n{stack_trace}")


def get_log_path():
    '''
    Function to replace '//' with '/' for logs path
    '''
    try:
        path = logs_folder_path + "/log.txt"
        return path.replace("//", "/")
    except Exception as e:
        critical_error_log("Failed getting log path! Assigning default logs path: './logs/log.txt'", e)
        return "./logs/log.txt"


__logs_file_path = get_log_path()


def print_lg(*msgs: str | dict, end: str = "\n", pretty: bool = False, flush: bool = False, from_critical: bool = False) -> None:
    '''
    Function to log and print messages.
    '''
    try:
        for message in msgs:
            pprint(message) if pretty else print(message, end=end, flush=flush)
            with open(__logs_file_path, 'a+', encoding="utf-8") as file:
                file.write(str(message) + end)
    except Exception as e:
        logging.error(f"Error writing to log file: {e}")
#>


def buffer(speed: int=0) -> None:
    '''
    Function to wait within a period of selected random range.
    '''
    if speed <= 0:
        return
    elif speed < 2:
        sleep(randint(6, 10) * 0.1)
    elif speed < 3:
        sleep(randint(10, 18) * 0.1)
    else:
        sleep(randint(18, round(speed) * 10) * 0.1)


def manual_login_retry(is_logged_in: callable, limit: int = 2) -> None:
    '''
    Function to ask and validate manual login.
    Replaced GUI-based alert with logging and CLI prompt.
    '''
    count = 0
    while not is_logged_in():
        logging.warning("Seems like you're not logged in!")
        print("Please log in manually.")
        input("Press Enter after you successfully log in.")
        count += 1
        if count > limit:
            logging.warning("Manual login confirmation failed. Skipping confirmation.")
            return


def calculate_date_posted(time_string: str) -> datetime | None | ValueError:
    '''
    Function to calculate date posted from string.
    '''
    time_string = time_string.strip()
    now = datetime.now()
    try:
        if "second" in time_string:
            seconds = int(time_string.split()[0])
            return now - timedelta(seconds=seconds)
        elif "minute" in time_string:
            minutes = int(time_string.split()[0])
            return now - timedelta(minutes=minutes)
        elif "hour" in time_string:
            hours = int(time_string.split()[0])
            return now - timedelta(hours=hours)
        elif "day" in time_string:
            days = int(time_string.split()[0])
            return now - timedelta(days=days)
        elif "week" in time_string:
            weeks = int(time_string.split()[0])
            return now - timedelta(weeks=weeks)
        elif "month" in time_string:
            months = int(time_string.split()[0])
            return now - timedelta(days=months * 30)
        elif "year" in time_string:
            years = int(time_string.split()[0])
            return now - timedelta(days=years * 365)
    except (ValueError, IndexError) as e:
        logging.error(f"Error parsing time string '{time_string}': {e}")
        return None


def convert_to_lakhs(value: str) -> str:
    '''
    Converts string value to lakhs.
    '''
    value = value.strip()
    l = len(value)
    if l > 0:
        if l > 5:
            return value[:l-5] + "." + value[l-5:l-3]
        else:
            return "0." + "0" * (5 - l) + value[:2]
    return "0.00"


def convert_to_json(data) -> dict:
    '''
    Function to convert data to JSON.
    '''
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        logging.error("Unable to parse the response as JSON")
        return {"error": "Unable to parse the response as JSON", "data": data}
