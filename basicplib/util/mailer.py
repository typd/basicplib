import smtplib
from email.mime.text import MIMEText
import threading

class Mailer:
    def __init__(self, smtp_host, from_addr=None):
        self.smtp = smtplib.SMTP(smtp_host)
        self.lock = threading.Lock()
        self.from_addr = from_addr

    def send(self, to_addr, subject, msg_str, from_addr=None):
        msg = MIMEText(msg_str)
        msg['Subject'] = subject
        if not from_addr:
            from_addr = self.from_addr
        msg['From'] = from_addr
        to_addrs = [to_addr] if type(to_addr) == str else to_addr
        msg['To'] = ','.join(to_addrs)
        try:
            self.lock.acquire()
            self.smtp.sendmail(from_addr, to_addrs, msg.as_string())
            self.smtp.quit()
            return True
        finally:
            self.lock.release()
