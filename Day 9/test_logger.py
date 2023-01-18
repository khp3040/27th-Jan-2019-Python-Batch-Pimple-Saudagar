import logging

FORMAT = '%(levelname)s: %(asctime)s %(lineno)d %(message)s'
logging.basicConfig(format=FORMAT, level=logging.ERROR, filename='today.log', filemode='w')

logging.debug('THIS is debug message')
logging.info('THIS is info message')
logging.warn('THIS is warn message')
logging.error('THIS is error message')
logging.critical('THIS is critical message')
