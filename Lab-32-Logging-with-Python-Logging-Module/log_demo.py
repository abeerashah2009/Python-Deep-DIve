import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w',
)

logging.debug('This is a debug message.')
logging.info('This is an info message.')
logging.warning('This is a warning message.')
logging.error('This is an error message.')
logging.critical('This is a critical message.')

def divide_numbers(a, b):
    try:
        result = a / b
        logging.info('Division successful.')
        return result
    except ZeroDivisionError:
        logging.exception('Division by zero error.')
        return None

result = divide_numbers(10, 0)
