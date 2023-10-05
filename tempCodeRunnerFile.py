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

import os
r="tempo"
def read_text_file(r):
    """Reading a file from the device"""
    try:
        with open(r, 'r') as file:
            content = file.read()  
        print(content) 
    except FileNotFoundError:
        print("File not found:",r )
    except IOError:
        print("Error reading the file:", r)
read_text_file(r)


def que():
    try:
        """ To count alpha and digit from the entered choice"""
        s=input("Please enter your choice accordingly:\n")
        c=0
        d=0
        for i in s:
            if i.isalpha():
                c=c+1
            if i.isdigit():
                d=d+1
        print("The count for alpha is {} and digit is {}".format(c,d))
    except Exception as e:
        print("An erro has occured in the system:\n",str(e))
que()
##### single line snipped for the counting
s="treiuiuw827873737"
sum(1 for x in s if x.isalpha() or x.isdigit())

len([x for x in range(90) if x%2==0])

def vowel_count():
    try:
        """Vowel count"""
        d=input("enter your choice you want to enter:\n")
        s=["A","a","E","e","i","I","O","o","U","u"]
        x=0
        for i in d:
            if i in s:
                x=x+1
        print("the total no of count is {}".format(x))
    except Exception as e:
        print("An error has occured which is {}".format(str(e)))
vowel_count()

def pelnedo():
    try:
        """ The palendrome function"""
        s=input("enter the choice for whom the pal is to be founs:\n")
        x=s[::-1]
        i=0
        for i in range(10):
            if x==s:
                print("The pal is found")
                break
            if i>=10:
                print("Limit is exceeded")
            if x!=s:
                pass
            print("please try again")
    except Exception as e:
        print("An error has been there which is {}".format(str(e)))
pelnedo()
            
            
def stut():
    try:
        d=input("Eneter the world for the stuttering to take place:\n")
        print(f"{d[:2]}....{d[:-2]}....{d[:3]}")
    except Exception as e:
        print(" An error has occured {}".format(str(e)))
stut()


def str():
    try:
        """ Program to print the stuttering of the words"""
        d=input("eneter the choice you want to be stuttered:\n")
        s=[lambda x : x, print(f"{d[:3]}....{d[:-2]}......{d[:4]}")]
        print(s)
    except Exception as e:
        print("An error has occured {}".format(str(e)))
str()


def maxn():
    try:
        """ This program prints the string with max length"""
        s=input("Max word count:\n")
        d=s.split()
        x=0
        for i in d:
            if len(i)>x:
                x=len(i)
                f=i    
        print("The word is maximum length is {}".format(f))
    except Exception as e:
        print("An error has occured {}".format(str(e)))
maxn()

def max_length_count():
    """ Max length counting function """
    s=input("eneter the statement to be counted\n")
    d=s.split()
    max=0
    for i in d:
        if len(i)>max:
            max=len(i)
            wer=i
    print("Max length is ",wer)
max_length_count()



try:
    def counting():
        s=input(" enter the choice to be counted\n")
        c=0
        for i in enumerate(s):
                c=c+1
        print("Total count are ",c)
except Exception as e:
    print(e)
counting()

str=input("enter a choice\n")
ransom=[(lambda x: x.upper()[::-1])]
print(ransom)


arr=[2,3,4,5,6,7]
zee=lambda x: x*7
c=list(map(zee,arr))
print(c)


s="Thomas anderson munro"
z=[lambda x : x.replace("thomas","Moron")]
print(z)
c=list(map(z,s))
print(c)


from functools import reduce
arr_list3 = [2,3,5,8,9]
sum_ele = lambda x,y : x*y

result_reduce = reduce(sum_ele,arr_list3)

print("Result of Reduce : ", result_reduce)


a=[2,3,4,5,6,7]
b=[7,6,5,4,3,2]
zip(a,b)
sum((x*y/2) for x,y in zip(a,b))


def rem(a=str,i=int):
    string=a.replace(a[i],'')
    return stre
rem("thomas",3)



### test it out for palendrome

def test():## program to match the nos
    try:
        a=int(input("enter a no of your choice\n:"))
        for i in range(10):
            c=0
            b=int(input("The choice to be matched\n:"))
            c=c+1
            if (a==b):
                print("you have found the right match so the process ends here.\n")
                break
            elif c>=10:
                print("You availed the maximum available chances, fuck off\n")
                break
            elif (a!=b):
                print("try again you have chances left",10-c)
    except Exception as e:
        print("An error has arrived, please pay heed to it", str(e))
test()
    

        
            
            































import os
r='tempo'
def file_read():
    try:
        with open(r,'r') as file:
            c=file.read()
            print(c)
    except Exception as e:
        print("An error has ocured",str(e))
file_read()



