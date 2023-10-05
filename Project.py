
#### to count the largest string
def largest():
    try:
        s=input("Enter your choice:\n")
        a=s.split()
        c=0
        for i in a:
            if len(i)>c:
                c=len(i)
                word=i
        print("The string with the largest value is {} ".format(word))
    except Exception as e:
        print("An error has been in the system", str(e))
largest()
## To count the vowels:
def vowels():
    """This program helps in counting th eno of vowels"""
    try: 
       s=input("Enter your choice:\n")
       d=["a","e","i","o","u"]
       c=0
       for i in s:
           if i in d:
               c=c+1
       print("The no of vowels in ypur choice is {}".format(c))
    except Exception as e:
        print(" There is an error which is {}".format(str(e)))
vowels()
### One liner 
s="Pumba and timon"
d=["a","e","i","o","u"]
sum(1 for i in s if i in d)
######The count of choice 
def count():
    try:
        """ This program is useful in finding the count of given choice"""
        d=input("Please enter your choice:\n")
        c=0
        for i in d:
            c=c+1
        print("The count is {}".format(c))
    except Exception as e:
        print("There has been error {}".format(c))
count()     
#### single line
s="There was a great hunter named Thomas"
sum(1 for x in s)
### Number mapping game:
def test():## program to match the nos
    try:
        """ The program helps a person find the right no in the game"""
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
                print("try again you have chances left",10-i)
    except Exception as e:
        print("An error has arrived, please pay heed to it", str(e))
test()
#### To print the treiangle patter:
def triangle():
    try:
        a=int(input("Enter a no of your choice for the triangle:\n"))
        for i in range(a-1):
             print("*"*i)
    except Exception as e:
        print("An error has occured due to {}".format(str(e)))
triangle()
## single line 
s =5
print('\n'.join(["*" * i for i in range(s)]))
###
import os
def reverse():
    try:
        with open('random','r') as file:
            
           lines=file.readlines()
        for lines in reversed(lines):
            print(lines.rstrip())
    except FileNotFoundError:
        print("File not found:", 'random')
    except IOError:
        print("Error reading the file:", 'random')
reverse()


import os
import platform, socket
print("Ip_adress:",socket.gethostbyname(socket.gethostname()))


socket.gethostbyname(socket.gethostname())
socket.gesthostbyname()
            
    
            
                  
