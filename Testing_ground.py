import logging
logging.basicConfig(filename='Project.logs', level=logging.DEBUG, format='%(asctime)s %(message)s %(output)s')
try: 
    
    def res(name):
        print("Hello",name)
except Exception as e:
    logging.error("An error has occured:\n")
    logging.exception("This has been cause due to", str(e))
try:
    def c_res():
        name=input("Enter your choice:\n")
        res(name)
except Exception as e:
    logging.error("An error has occured:\n")
    logging.exception("This has been cause due to", str(e))
c_res()

def greet(name):
    print("Hello,", name)

def call_greet():
    name = input("Enter your name: ")
    greet(name)

call_greet()
## python function to shut down your system

import os

def shutdown_system():
    try:
        os.system("shutdown /s /t 0")
    except Exception as e:
        print("An error occurred while shutting down the system:", str(e))
        
## python function to print the system configuration
import logging
logging.basicConfig(filename="Project.logs", level=logging.DEBUG, format='%(asctime)s %(message)s %(output)s')
import platform
try:
    def sys_config():
        system=platform.system()
        node=platform.node()
        processor=platform.processor()
        architecture=platform.architecture()
        print("system:",system)
        print("node:",node)
        print("processor:",processor)
        print("architecture:",architecture)
except Exception as e:
    logging.error("An exception has occured")
    logging.exception("This has arised due to:\n", str(e))
sys_config()     

## function to write and access an email
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
            server.send_message(email)
        logging.info("the email was shot with success")
    except Exception as e:
        logging.error("There is some error")
        logging.exception("This has been due to:\n", str(e))
send_mail()          
    
    
    
    


def send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port):
    logging.basicConfig(filename='email.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Create an instance of EmailMessage
        email = EmailMessage()
        email['From'] = sender_email
        email['To'] = receiver_email
        email['Subject'] = subject
        email.set_content(message)

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Log in to the SMTP server if authentication is required
            # server.login(smtp_username, smtp_password)

            # Send the email
            server.send_message(email)

        logging.info('Email sent successfully.')
    except Exception as e:
        logging.error(f'Error sending email: {str(e)}')

# Example usage
sender_email = 'your_email@example.com'
receiver_email = 'recipient@example.com'
subject = 'Hello, World!'
message = 'This is a test email sent from Python.'
smtp_server = 'smtp.example.com'
smtp_port = 587

send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port)

    
   
        
