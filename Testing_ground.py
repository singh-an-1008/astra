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
    
    
    
    




    
   
        
