import logging
import os
from datetime import datetime 


# Configure the logger
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s: %(message)s')

# Create a logger object
logger = logging.getLogger(__name__)

# Define log levels
# logger.debug('This is a debug message')  # Uncomment for debug messages
# logger.info('This is an info message')    # Uncomment for info messages
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

# Example usage in a script
if __name__ == "__main__":
    logger.info('Logger initialized successfully')
    try:
        result = 10 / 0  # Simulate an error
    except Exception as e:
        logger.error('An error occurred: %s', str(e))
