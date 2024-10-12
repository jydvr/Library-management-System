import logging
from datetime import datetime

class Metering:
    try:
        def __init__(self, level=logging.INFO):
            current_date = datetime.now().strftime('%d-%m-%Y')
            log_files = f'{current_date}meteringlog.log'
            
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(level)
    
            file_handler = logging.FileHandler(log_files)
            formatter = logging.Formatter(  "{asctime} | {levelname} | GBB | System | {module} | {filename} | {funcName} | {message} |",
                        style="{",
                    )
            file_handler.setFormatter(formatter)
        
            self.logger.addHandler(file_handler)
    except Exception as e:
        print(e)
    def get_log(self):
        try:
            return self.logger
        except Exception as e:
            print(e)