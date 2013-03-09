import tempfile

from basicplib.util.logger import create_default_logger


def test_create_default_logger():
    path = tempfile.NamedTemporaryFile()
    logger = create_default_logger(path=path.name)
    logger.info('log msg')
    logger.debug('log msg')
    
