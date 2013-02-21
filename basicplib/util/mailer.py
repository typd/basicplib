import smtplib
from email.MIMEText import MIMEText
import threading

class Mailer:
    def __init__(self, smtp_host):
        self.smtp = smtplib.SMTP(smtp_host)
        self.lock = threading.Lock()  

    def send(self, from_addr, to_addr, subject, msg_str):
        msg = MIMEText(msg_str)
        msg['Subject'] = subject
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
