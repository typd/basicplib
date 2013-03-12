import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders as Encoders

def send(smtp_host, send_from, send_to, subject, text,
        files=None, text_type="plain"):
    """ 
    based on http://snippets.dzone.com/posts/show/2038
    attachments can be specified as a list of strings [file_name, ...] or a list of tuples
    containing intended names and file data [(file_name, data), ...]
    """
    assert type(send_to) == list
    msg = MIMEMultipart()
    msg['From'] = send_from 
    msg['To'] = ', '.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text, text_type))
    for _file in files:
        if type(_file) is tuple:
            name, data = _file
        else:
            name = _file
            data = open(name,"rb").read()
        part = MIMEBase('application', "octet-stream")
        part.set_payload(data)
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{}"'
                .format(os.path.basename(name)))
        msg.attach(part)
    smtp = smtplib.SMTP(smtp_host)
    smtp.sendmail(send_from, send_to, msg.as_string())
