from datetime import datetime
import time
import logging
from basicplib.util.file import ensure_path

_DEFAULT_PATH = "log/%s.log" % (datetime.utcnow().strftime('%Y-%m-%d'))

def create_default_logger(path=_DEFAULT_PATH):
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)
    logging.Formatter.converter = time.gmtime
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    ensure_path(path)
    fhandler = logging.FileHandler(path)
    fhandler.setLevel(logging.INFO)
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
    chandler = logging.StreamHandler()
    chandler.setLevel(logging.DEBUG)
    chandler.setFormatter(formatter)
    logger.addHandler(chandler)
    return logger

