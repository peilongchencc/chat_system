import logging
from logging.handlers import RotatingFileHandler
from scrapy.utils.project import get_project_settings

def setup_logging():
    settings = get_project_settings()
    log_file_path = settings.get('CUSTOM_LOG_FILE', 'scrapy_log_custom.txt')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = RotatingFileHandler(log_file_path, maxBytes=10*1024*1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger
