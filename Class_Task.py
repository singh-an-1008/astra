## A function using another function:
import logging
logging.basicConfig(filename='Project.logs', level=logging.DEBUG, format='%(asctime)s %(message)s %(output)s')
try: 
    
    def res(name):
        """ this function calls another function """
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
        """ This function will shutdown the system"""
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
            server.send_message(mail)
        logging.info("the mail was shot with success")
    except Exception as e:
        logging.error("There is some error")
        logging.exception("This has been due to:\n", str(e))
send_mail()          
# Example usage
s_mail = "your mail adress"
r_mail = 'receivers_mail'
sub = 'Mail testing'
message = 'Trying things in python functions.'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
send_mail(s_mail, r_mail, sub, message, smtp_server, smtp_port)

#### function to print the index:
def index():
    try:
        """ This function prints the index of the entered choice"""
        s=input("Enter a choice of yours:\n")
        for i in enumerate(s):
            print(i)
    except Exception as e:
        print("The error has been due to", str(e))
index()
#### String Count function:
def lenf():
    try:
        """This functions counts the length of the enetered string"""
        a=input("Please eneter your choice:\n")
        q=0
        for i in a:
            if type(a)==str():  
                q=q+1
        print("The length of the entered string is {}".format(q))
    except Exception as e:
        print("An error has occured,",str(e))
lenf()
##### Function to print the primitive index:
def all_index():
    try:
        """ Function to print all the primitive index of the entered choice"""
        f=input("Please enter your choice accordingly:\n")
        if type(f) in [list,tuple,set,str,dict]:
            for i in enumerate(f):
              print("The index of the enetered choice is {}".format(i))
    except Exception as e:
        print("An error has occured,",str(e))
all_index()

#### Input as dict and output as list:
def dictr():
    try:
        """ Function takes dict as input an returns list as a output"""
        s=(input("Enter your choice:\n"))
        l=[]
        if type(s)==dict:
            for i in s.values():
                l.append(i)
                print(l)
    except Exception as e:
        print("An error has occured:",str(e))
dictr()
#### Function to cancatenate list:
def list_join(*agrs):
    try:
        """ This will concatenat the list"""
        s=[]
        for i in agrs:
            if type(i)==list:
                s.extend(i)
            return s
    except Exception as e:
        print("An erro has occured:\n",str(e))
list_join()

#### Input list and [rint index even in case of repetition:
def task_list():
    try:
        """Take a list as an input return an index of each element like a inbuilt index function 
    but even if we have repetative element it should return index"""
        s=input("Enter the choice:\n")
        a={}
        if type(s)==list:
           for i,j in enumerate(s):
              a[j].append(i)
              return a
    except Exception as e:
        print("An error has occured",str(e))
task_list()

#### Function returning all names from dir:
import os
def file_name():
    try:
        """ Returning all the names from dir"""
        file_path=input("Please enter the path of dir:\n")
        if os.path.exists(file_path):
            for f in os.listdir(file_path):
                print(f)
    except Exception as e:
        print("An erro has occured",str(e))
file_name()

### Function to show system Configuration:
import os
import platform,socket
def Sys_info():
    try:
        """ This will tell the system info"""
        Admin=platform.uname()
        print(Admin)
        print("System:",platform.system())
        print("Release:",platform.release())
        print("version:",platform.version())
        print("processor:",platform.processor())
        print("Architecture:",platform.machine())
        print("Hostname:",socket.gethostname())
        print("Ip_adress:",socket.gethostbyname(socket.gethostname()))
    except Exception as e:
        print("An error has occured, please look into it:",str(e))
Sys_info()
#### function to get todays date time:
import datetime
import pandas as pd
def date_time():
    try:
        """ This function will give the date time"""
        s=pd.Timestamp.now()
        return s
    except Exception as e:
        print("An error has occured",str(e))
date_time()

#### Pyhton function to read an image:
import os
from PIL import Image
def img_read():
    try:
        """ This will read the imgae for us"""
        f_path=input("Please eneter the path of the image:\n")
        if not os.path.isfile(f_path):
            print("The specified path does not exist")
            return None
        img=Image.open(f_path)
        return img
    except Exception as e:
        print("An error has occured:\n",str(e))
img_read()

### This function  to play the video file:
import os
import pygame
def video_play():
    try:
        """ This function will play the video file for us"""
        pygame.init()
        video_info = pygame.display.Info()
        screen_width = video_info.current_w
        screen_height = video_info.current_h
        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("Video Player")
        video = pygame.Movie.Movie(file_path)
        video.set_display(screen)
        video.play()
        while video.get_busy():
            pygame.time.Clock().tick(30)
        pygame.quit()
    except Exception as e:
        print("An error occurred while playing the video:", str(e))
video_play()

#### Python function to move a dir ftom one place to another:
import os,shutil
def move():
    try:
        """ Copying a file from one dir to other"""
        a=input("Enter the path of first dir:\n")
        b=input("Enter the path of second dir:\n")
        shutil.move(a,b)
        print(" The opeartion was successful")
    except Exception as e:
        print("An error has occured",str(e))
move()

#### Python function to read the pdf file:
import PyPDF2
def read_pdf():
    try:
        """ Python function to raed a pdf file"""
        s=input("Please eneter the file path:\n")
        with open (s,"rb") as file:
            c=PyPDF2.PdfFileReader(file)
            pages_num = pdf_reader.numPages
            con_tex=""
            for page_num in range(pages_num):
                page = pdf_reader.getPage(page_num)
                con_tex += page.extractText()
                return con_tex.strip()
    except Exception as e:
        print("An error occurred while reading the PDF file:", str(e))
read_pdf()

### Python function to merge two pdf files:
from PyPDF2 import PdfMerger
def blend(f1,f2,f3):
    try:
        """ function will blen 2 file"""
        merger=PdfMerger()
        with open(f1,"rb") as file1:
            merger.append(file1)
        with open(f2,"rb") as file2:
            merger.append(file2)
        with open (f3,"wb") as file3:
            merger.write(file3)
        print(" The operation was successful:")
    except Exception as e:
        print("An error has exception has occured:",str(e))
blend()
### Python function to print the ip adress:
import platform,os,socket
def ip_adress():
    try:
        """ this will print the ip adress of the system"""
        a=platform.uname()
        print(a)
        print("Ip_adress:",socket.gethostbyname(socket.gethostname()))
    except Exception as e:
        print(" There has been an exception in the program:",str(e))
ip_adress()

### This will read only word file from dir:
import os
def w_found(dir):
    try:
        """ The will read only the docx file list"""
        w_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.doc') or file.endswith('.docx'):
                    w_files.append(os.path.join(root, file))
        return w_files
    except Exception as e:
        print("An error occurred while searching for Word files:", str(e))
w_found()

##### Python function to print the word file:
import docx
def word_read():
    try:
        """ this will read the content of the word file"""
        s=input("Enter the path please:")
        d=docx.Document(s)
        for i in d.paragraphs:
            print(i.text)
    except Exception as e:
        print("An error occurred while reading the Word file:", str(e))
word_read()

print(" Thank you for your precious time in reviewing, feedback will be highly valued")


            
            
        
        
        
                
                
        
        
            
        
                
                

    
   
        
