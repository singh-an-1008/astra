import logging
logging.basicConfig(filename='Project.logs', level=logging.DEBUG, format='%(asctime)s %(message)s %(output)s')
try: 
    def res(name):
        logging.info("Hello",name)
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
## Rest next daydsknlkgs

## Doing things/ testing g