import logging
from datetime import datetime
## logging settings

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers= [
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

with open("app1.log", "a") as f:
    f.write("PROGRAM STARTED\n")

def add(x, y):
    result = x + y
    logger.debug(f"Add: {x} + {y} = {result}")  
    return result

def subtract(x, y):
    result = x - y
    logger.debug(f"Subtract: {x} - {y} = {result}")  
    return result

def multiply(x, y):
    result = x * y
    logger.debug(f"Multiply: {x} * {y} = {result}")  
    return result

def divide(x, y):
    try:
        result = x / y
        logger.debug(f"Dividing {x} / {y} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is not allowed.")
        return None

add(4, 24)
subtract(24, 4)
multiply(4, 24)
divide(24, 0)

with open("app1.log", 'a') as f:
    f.write("PROGRAM ENDED\n")
    f.write(f"{'-' * 80}\n")