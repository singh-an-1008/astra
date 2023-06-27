def hello():
    print("Hwllo Buddy how are you:")
hello()
print("Hello Hunt")

import smtplib
import logging
from email.message import EmailMessage
logging.basicConfig(filename="Project.logs", level=logging.INFO, format='%(asctime)s %(message)s %(output)s')
def send_mail(s_mail,r_mail,sub, smtp_server,smtp_port,message):
    try:
        mail=EmailMessage()
        mail['From']=s_mail
        mail['To']=r_mail
        mail['Subject']=sub
        mail.set_content(message)
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.send_message(mail)
        logging.info("the mail was shot with success")
    except Exception as e:
        logging.error("There is some error")
        logging.exception("This has been due to:\n", str(e))
send_mail() 