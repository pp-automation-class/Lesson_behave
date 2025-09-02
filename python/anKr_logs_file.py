import logging

LOG_MESSAGE = "This message will not go to the log file"

logging.basicConfig(filename='ankr_example.log', level=logging.DEBUG,       # Suggested, and it is builded in Python
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )

logging.debug("This message will go to the console")
logging.info("This message will go to the log file")
# logging.warning("This message will not go to the log file")
# logging.error("This message will not go to the log file")
# logging.critical("This message will not go to the log file")
# DRY - Don't Repeat Yourself,
# so to prevent repeating the same string for warning, error, and critical I created a variable LOG_MESSAGE
logging.warning(LOG_MESSAGE)
logging.error(LOG_MESSAGE)
logging.critical(LOG_MESSAGE)
"""
Level       Description
# ===================================================================
# DEBUG       Detailed debugging information
# INFO        General information about program flow
# WARNING     Something went wrong, but it’s not critical
# ERROR       An error that prevents part of the program from working
# CRITICAL    A critical error that may stop the program entirely
# Automatically generated description of the levels above and changed example.log file's name to ankr_example.log
"""
# Detailed use of that logs in test files will be in Session 18.
