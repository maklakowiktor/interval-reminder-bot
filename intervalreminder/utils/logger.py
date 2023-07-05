# Usage example:
# from utils.logger import logger

# # Log an info message
# logger.info('This is an info message')

# # Log a warning message
# logger.warning('This is a warning message')

# # Log an error message with an exception traceback
# try:
#     1 / 0
# except ZeroDivisionError as e:
#     logger.error('An error occurred: %s', e, exc_info=True)


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('bot.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)