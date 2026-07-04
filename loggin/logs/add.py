from logger import logging

def add(a, b):
    logging.info(f"Adding {a} and {b}")
    print( a + b)

logging.debug("the add function is called")
add(4, 3332)
