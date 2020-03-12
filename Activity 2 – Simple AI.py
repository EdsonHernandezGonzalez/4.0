# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:44:18 2020

@author: edson
"""
Base_name ="EDSON"
username = None
age = None
phone=None
blood = None
tuition=None
Sex= None
Email = None
print ("what is your name?")
username = input(f"({username})")

print (f"Hello, {username}, my name is {Base_name}")

    
answer = input("how old are you?")
age= input(f"({age}):")
    
answer = input("Can you tell me your tuition?(y/n)")
tuition= input(f"({tuition})New tuition:")
    
answer =  input ("Can you tell me your phone number?(y/n)") 
if answer == "y":
    phone= input(f"({phone})New phone:")
    
answer = input ("What is your blood type?")
blood = input(f"({blood})")
answer =  input ("What is your sex? You cannot answer the question if you want.(y/n)") 
if answer == "y":
    Sex = input(f"({Sex}):")
    
answer =  input ("Do you want your information to be sent to your email?.(y/n)") 
if answer == "y":
    Email= input(f"({Email}):")


    

print("Your credential is ready tomorrow, let's verify your data.")
print(f"(username:)({username})")
print(f"(age:)({age})")
print(f"(phone:)({phone})")
print(f"(blood:)({blood})")
print(f"(tuition:)({tuition})")
print(f"(Sex:)({Sex}))")
print(f"Is your information correct?(y/n)")
if answer == "y":
    print("your ID is ready.")



    