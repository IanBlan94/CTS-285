# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:00:21 2024

@author: isbla
"""

# DataMan
# 09/14/2024
# CTS-285 Norris
# Ian Blanchard


def menu():
    print("1) Answer Checker")
    print("2) Memory Bank")
    print("3) Exit")
    
def main():
    while True:
        menu()
        choice = input("Please enter a number choice from the menu: ")
        
        if choice == "1":
            answer_checker()
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Please enter a correct response")
            

    
def answer_checker():
    
    print("Welcome to your favorite answer checker! " 
          "Where we get silly and weird with numbers!")
    while True:
        try:
            # Get user input for the full equation (e.g., "1 + 1 = 2")
            equation = input("Enter a full equation (e.g., 1 + 1 = 2): ")
            
            # Split the equation into the left-hand side and right-hand side
            if '=' not in equation:
                print("Please enter an equation with '='.")
                return
            
            lhs, rhs = equation.split('=')
    
            # Strip whitespace and evaluate the left-hand side (LHS)
            lhs = lhs.strip()
            correct_answer = eval(lhs)
    
            # Strip whitespace and convert the right-hand side (RHS) to a float
            rhs = rhs.strip()
            user_answer = float(rhs)
            
            # Compare the evaluated left-hand side with the user-provided right-hand side
            if correct_answer == user_answer:
                print("Correct! Well done!")
            else:
                print(f"Incorrect. The correct result for {lhs} is {correct_answer}, but you entered {user_answer}.")
        
        except (SyntaxError, NameError):
            print("Invalid equation format. Please try again.")
        except ValueError:
            print("Please enter a valid number for the right-hand side.")
        except ZeroDivisionError:
            print("Error: Division by zero is undefined.")
            
        choice = input("Do you want to do another problem? (yes or no)").lower()
        
        if choice == "yes":
            pass
        else:
            break

if __name__ == "__main__":
    main()
