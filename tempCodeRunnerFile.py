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
## python program to read the index no
print(" Hello World :/n"*4)
def loop():
    s=input("enter your choice:/n")
    a=0
    while a<=4:
        a=a+1
        print(s)
loop()
[ print("tri") for x in range(4)]
[ "tri" for x in range(4)]
def index():
    try:
        s=input("Enter a choice of yours:\n")
        for i in enumerate(s):
            print(i)
    except Exception as e:
        print("The error has been due to", str(e))
index()
####################################################
try:
    """ This function gives the index of the words entered """
    def reverse():
        T=input("Enter your choice")
        for i in range(len(T)-1,-1,-1):
            print(i,T[i])
        return
    reverse()
except Exception as e:
    print(e)


import sys
print(sys.argv[1])
import time
time.asctime()








###
x=lambda x: x ** 3, 2, 3
print(x)
cube=lambda x: x ** 3, 2, 3
f(cube, 2,3);

x=92 
if x%2==0 :
    print("lullaby")
x=92; print("greaet") if x%2==0 else print("pumbs")
a=[2,3,4,5,6,7,8,8]
[x*2 for x in a if x%2==0 ]
s=[2,3,4,5,6]
x=[4,5,6,7,8]
a=zip(s,x)
[ i[0] +i[1] for i in a]
a="bukka reddy"
[ x  for x in enumerate(a)]
a=["pumba","timon","raskekamar"]
s.split(a)
len(s)

import os
def readt(tempo):
    try:
        with open('tempo','r') as files:
            content=files.read()
            print(content)
    except Exception as e:
        print("An error has occured",str(e))
readt('tempo')


def read_text_file(tempo):
    try:
        with open(tempo, 'r') as file:
            content = file.read()  # Read the entire file content

        print(content)  # Print or process the content as needed

    except FileNotFoundError:
        print("File not found:", )
    except IOError:
        print("Error reading the file:", filename)

read_text_file(tempo)
