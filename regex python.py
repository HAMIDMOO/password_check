
import re

Name= input("Enter Your Name :")
ID= input("Enter Your ID number :")
number= input("Enter Your Mobile number :")


def replay():
    password= input("Enter Your password :")
    
    check_1= re.search(Name, password)
    check_2= re.search(ID, password)
    check_3= re.search(number, password)
    if check_1 :
        print("your password is have a pice of your Name !!!")
    elif check_2:
        print("your password is have a pice of your ID number !!!")
    elif check_3 :
        print("your password is have a pice of your mobile number !!!")
    else:
        print("the works completed")
    x=input("do you want to try again??")  
    if x == "Y":
        replay() 

replay()