# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:03:36 2024

@author: isbla
"""
#/// CTS 285
#// M1H1
#// Ian Blanchard
#// 08/20/2024
def menu():
    print("-"*10 + "Menu Options" + "-"*10)
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit")
    
def main():
    repeat = True
    while repeat == True:
       
        menu()
        choice = input("Please enter a number from the menu ")
        
        if choice == "1":
            while True:
                numbers = get_numbers()
                result = addition(numbers)
                print(f"{numbers[0]} + {numbers[1]} = {result}")
                while True:
                    choice = input("Would you like to  add another problem? yes or no? ").lower()
                    if choice == "yes":
                        break
                    elif choice == "no":
                        break
                    else:
                        print("Please pick an appropiate response.\n ")
                if choice == "no":
                    break
            
            
        elif choice == "2":
            
            while True:
                numbers = get_numbers()
                result = subtraction(numbers)
                print(f"{numbers[0]} - {numbers[1]} = {result}")
                
                while True:
                    choice = input("Would you like to  do another problem? yes or no? ").lower()
                    if choice == "yes":
                        break
                    elif choice == "no":
                        break
                    else:
                        print("Please pick an appropiate response")
                if choice == "no":
                    break
        elif choice == "3":
            
            while True:
                numbers = get_numbers()
                result = multiplication(numbers)
                print(f"{numbers[0]} * {numbers[1]} = {result}")
                
                while True:
                    choice = input("Would you like to do another problem? yes or no? ").lower()
                    if choice == "yes":
                        break
                    elif choice == "no":
                        break
                    else:
                        print("Please pick an appropiate response")
                if choice == "no":
                    break
                
        elif choice == "4":
            
            while True:
                numbers = get_numbers()
                result = division(numbers)
                print(f"{numbers[0]} * {numbers[1]} = {result}")
                
                while True:
                    choice = input("Would you like to do another problem? yes or no? ").lower()
                    if choice == "yes":
                        break
                    elif choice == "no":
                        break
                    else:
                        print("Please pick an appropiate response")
                if choice == "no":
                    break
                       
        elif choice == "5":
            print("Thank you for using our calculator!")
            repeat = False
        else:
            print("Please enter a number 1-5 from the menu options")
            
        
def addition(stored):
    total = stored[0]
    for i in stored[1:]:
        total += i
    return total
  
            
def subtraction(stored):
    total = stored[0]
    for i in stored[1:]:
        total -= i
    return total
               
def multiplication(stored):
        total = stored[0]
        for i in stored[1:]:
            total *= i
        return total    
 
def division(stored):
    for i in stored[0:]:
        if i == 0:
            print("Cannot divide by zero\n")
            return None
    total = stored[0]
    for i in stored[1:]:
        total /= i
    return total 
           
def get_numbers():
    stored = []
    one = int(input("Please enter the first number \n"))
    two = int(input("Please enter the second number \n"))
    stored.append(one)
    stored.append(two)
    return stored
        
main()
    
 
