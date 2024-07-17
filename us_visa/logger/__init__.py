# Importing the logging module to enable logging functionality
import logging

# Importing the os module for interacting with the operating system
import os

# Importing the from_root function to get the root directory of the project
from from_root import from_root

# Importing the datetime module to work with date and time
from datetime import datetime

# Generating a log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Defining the directory name where logs will be stored
log_dir = 'logs'

# Constructing the full path for the log file within the logs directory
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Creating the logs directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Configuring the logging settings such as log file path, format, and log level
logging.basicConfig(
    filename=logs_path,  # Setting the file where logs will be written
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",  # Defining the log message format
    level=logging.DEBUG,  # Setting the logging level to DEBUG to capture all levels of log messages
)
