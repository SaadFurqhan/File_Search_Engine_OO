import logging
import sys
sys.path.append('.')

#Error log if any occurs
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('../Logger/error.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


#Console Log
logging.basicConfig(filename='../Logger/console_records.log',level=logging.DEBUG,format='%(asctime)s: %(name)s: %(message)s')
