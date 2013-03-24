import tempfile

from basicplib.util.logger import create_default_logger


def test_create_default_logger():
    tempf = tempfile.NamedTemporaryFile()
    logger = create_default_logger(path=tempf.name)
    logger.info('info msg')
    logger.debug('debug msg')
    logger.warn('warn msg')
    logger.error("error msg")
    logger.critical("critical msg")
    try:
        raise RuntimeError("Opa!")
    except RuntimeError as exc:
        logger.exception(exc)
    tempf.close()
    
