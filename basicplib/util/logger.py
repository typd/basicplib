import sys
import time
import logging
from datetime import datetime

from logutils.colorize import ColorizingStreamHandler

from basicplib.util.file import ensure_path


_DEFAULT_PATH = "log/%s.log" % (datetime.utcnow().strftime('%Y-%m-%d'))


class RainbowLoggingHandler(ColorizingStreamHandler):
    """ A colorful logging handler optimized for terminal debugging aestetichs.
    - Designed for diagnosis and debug mode output - not for disk logs
    - Highlight the content of logging message in more readable manner
    - Show function and line, so you can trace where your logging messages
      are coming from
    - Keep timestamp compact
    - Extra module/function output for traceability
    The class provide few options as member variables you
    would might want to customize after instiating the handler.
    """
    __author__ = "Mikko Ohtamaa <mikko@opensourcehacker.com>"
    __license__ = "MIT"

    # Define color for message payload
    level_map = {
        logging.DEBUG: (None, 'white', False),
        logging.INFO: (None, 'black', False),
        logging.WARNING: (None, 'yellow', True),
        logging.ERROR: (None, 'red', True),
        logging.CRITICAL: ('red', 'red', True),
    }

    date_format = "%m-%d %H:%M:%S"

    #: How many characters reserve to function name logging
    who_padding = 20

    #: Show logger name
    show_name = True

    def get_color(self, fontg=None, backg=None, bold=False):
        """
        Construct a terminal color code
        :param fg: Symbolic name of foreground color
        :param bg: Symbolic name of background color
        :param bold: Brightness bit
        """
        params = []
        if backg in self.color_map:
            params.append(str(self.color_map[backg] + 40))
        if fontg in self.color_map:
            params.append(str(self.color_map[fontg] + 30))
        if bold:
            params.append('1')
        color_code = ''.join((self.csi, ';'.join(params), 'm'))
        return color_code


    def colorize(self, record):
        """
        Get a special format string with ASCII color codes.
        """
        # Dynamic message color based on logging level
        if record.levelno in self.level_map:
            fontg, backg, bold = self.level_map[record.levelno]
        else:
            # Defaults
            backg = None
            fontg = "black"
            bold = False
        # Magician's hat
        # https://www.youtube.com/watch?v=1HRa4X07jdE
        template = [
            self.get_color("white", None, True), "[%(asctime)s] ",
            self.reset,
            self.get_color(backg, fontg, bold),
            "%(message)s ",
            self.reset,
            "%(padded_who)s",
            self.reset,
        ]
        thisformat = "".join(template)
        who = [self.get_color("white"),
               getattr(record, "funcName", ""),
               "()",
               self.get_color("white", None, False),
               ":",
               self.get_color("white"),
               str(getattr(record, "lineno", 0))]
        who = "".join(who)
        # We need to calculate padding length manualy
        # as color codes mess up string length based calcs
        unformatted_who = getattr(record, "funcName", "") + "()" + \
            ":" + str(getattr(record, "lineno", 0))
        if len(unformatted_who) < self.who_padding:
            spaces = " " * (self.who_padding - len(unformatted_who))
        else:
            spaces = ""
        record.padded_who = who + spaces
        formatter = logging.Formatter(thisformat, self.date_format) 
        self.colorize_traceback(formatter, record)
        output = formatter.format(record)
        # Clean cache so the color codes of traceback
        # don't leak to other formatters
        record.ext_text = None
        return output


    def colorize_traceback(self, formatter, record):
        """
        Turn traceback text to red.
        """
        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)
            record.exc_text = "".join([
                self.get_color("red"),
                formatter.formatException(record.exc_info),
                self.reset,
            ])


    def format(self, record):
        """
        Formats a record for output.
        Takes a custom formatting path on a terminal.
        """
        if self.is_tty:
            message = self.colorize(record)
        else:
            message = logging.StreamHandler.format(self, record)
        return message


def create_default_logger(path=_DEFAULT_PATH):
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)
    logging.Formatter.converter = time.gmtime
    
    ensure_path(path)
    fhandler = logging.FileHandler(path)
    fhandler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(message)s", '[%m-%d %H:%M:%S]')
    fhandler.setFormatter(formatter)

    logger.addHandler(fhandler)
    chandler = RainbowLoggingHandler(sys.stdout)
    logger.addHandler(chandler)
    return logger

