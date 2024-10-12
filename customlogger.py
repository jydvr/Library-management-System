import logging
from datetime import datetime
class CustomLogger:
    try:
        def __init__(self , level=logging.INFO):
            current_date = datetime.now().strftime('%d-%m-%Y')
            log_file = f'{current_date}applicationlog.log'
            
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(level)
    
            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(module)s | %(funcName)s | %(message)s')
    
            file_handler.setFormatter(formatter)
    
            self.logger.addHandler(file_handler)
    except Exception as e:
        print(e)
    def get_logger(self):
        try:
            return self.logger
        except Exception as e:
            print(e)