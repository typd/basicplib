from datetime import date
import logging
from file import ensure_path

default_path = "log/%s.log" % (date.today().isoformat())

def create_default_logger(path=default_path):
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    ensure_path(path)
    fh = logging.FileHandler(path)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


