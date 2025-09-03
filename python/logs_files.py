import logging

logging.basicConfig(filename='example.log', level=logging.INFO,
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )

logging.debug("This message will also go to the console")
logging.info("This message will go to the log file")
logging.warning("This message will not go to the log file")
logging.error("This message will not go to the log file")
logging.critical("This message will not go to the log file")

"""
Level       Description
===================================================================
DEBUG       Detailed debugging information
INFO        General information about program flow
WARNING     Something went wrong, but it’s not critical
ERROR       An error that prevents part of the program from working
CRITICAL    A critical error that may stop the program entirely
"""
