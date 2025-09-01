import os
import sys
import logging
from logging.handlers import RotatingFileHandler

LOG_FORMAT = "[%(asctime)s]: [%(levelname)s]: [%(name)s]: [%(message)s]"
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "running_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("textSummarizerLogger")
logger.setLevel(logging.INFO)


if not logger.handlers:
    formatter = logging.Formatter(LOG_FORMAT)

    
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5_000_000, backupCount=5)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
