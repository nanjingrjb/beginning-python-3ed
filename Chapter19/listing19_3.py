import logging

logging.basicConfig(level=logging.INFO, filename='mylog.log')

logging.info('Starting program')

logging.info('Trying to divide 1 by 0')
try:
    print(1 / 0)
except Exception as e:
    logging.info('发生异常，信息为:')
    
    logging.info(e)

logging.info('The division succeeded')

logging.info('Ending program')
