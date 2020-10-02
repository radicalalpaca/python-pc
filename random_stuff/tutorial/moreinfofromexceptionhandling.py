import sys
import logging

def error_handling():
    return f"{sys.exc_info()[0].__name__}. {sys.exc_info()[1]}, line {sys.exc_info()[2].tb_lineno}."

try:
    a + b
except Exception as e:
    logging.error(error_handling())