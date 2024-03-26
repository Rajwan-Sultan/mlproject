import sys
from src.mlproject.logger import logging
from src.mlproject.exceptions import CustomException


if __name__ == "__main__":
    logging.info("The execution has started!")

    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception has been raised!")
        raise CustomException(e,sys)

    pass