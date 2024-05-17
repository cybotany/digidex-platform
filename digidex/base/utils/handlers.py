import os
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


class CustomTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, base_log_dir, *args, **kwargs):
        self.base_log_dir = base_log_dir
        # Set a temporary filename during initialization
        temp_filename = os.path.join(base_log_dir, 'temp.log')
        super().__init__(temp_filename, *args, **kwargs)

    def _open(self):
        # Get the current year and month
        current_time = datetime.now()
        year = current_time.strftime('%Y')
        month = current_time.strftime('%B')
        day_name = current_time.strftime('%A')
        day = current_time.strftime('%d')
        
        # Create year/month directories
        log_dir = os.path.join(self.base_log_dir, year, month)
        os.makedirs(log_dir, exist_ok=True)
        
        # Set the filename with the day
        self.baseFilename = os.path.join(log_dir, f'{day_name}-{day}.log')
        return super()._open()
