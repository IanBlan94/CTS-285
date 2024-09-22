# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:00:21 2024

@author: isbla
"""
import random

def menu():
    print("1) Answer Checker")
    print("2) Memory Bank")
    print("3) Exit")
    
def choice():
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
            
def math_menu():
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit to main menu")
    
def answer_checker():
    
    print("Welcome to your favorite answer checker! " 
          "Where we get silly and weird with numbers!")
    
    print("Which type of math problems would you like to practice on?")
    while True:
        math_menu()
        choice = input("Please enter a number choice from the menu: ")
        
        if choice == "1":
            addition_checker()
        elif choice == "2":
            subtraction_checker()
        elif choice == "3":
            multiplication_checker()
        elif choice == "4":
            division_checker()
        elif choice == "5":
            break
        else:
            print("Please enter a correct response")
    
def generate_num(operation, range_min=1, range_max=100):

    num1 = random.randint(range_min, range_max)
    num2 = random.randint(range_min, range_max)
    if operation == '/' and  num1 == 0 or num2 == 0:
      num2 = random.randint(1, range_max) 
      num1 = random.randint(1, range_max)
      # Re-roll num2 if it's 0 for division
    return num1, num2, operation

def addition_checker():
    
    print("Let's do some addition!")
    correct_counter = 0
    problems_solved = 0
    max_problems = 3  # Number of problems to solve

    while problems_solved < max_problems:
        num1, num2, oper = generate_num("+", 1, 100)  # Correct assignment order
        print(f'What is {num1} + {num2}? ')
        correct_answer = num1 + num2
        attempts = 0
        max_attempts = 3  # Number of guesses allowed

        while attempts < max_attempts:
            try:
                user_answer = float(input("Please enter an answer: "))
            except ValueError:
                print("Invalid input, please enter a valid number.")
                continue  # Continue the loop without counting the attempt

            if int(user_answer) == correct_answer:
                print("Correct! Well done!")
                correct_counter += 1
                break
            else:
                attempts += 1
                if attempts < max_attempts:
                    print(f"Incorrect. Try again. You have {max_attempts - attempts} attempts left.")

        if attempts == max_attempts:
            print(f"Sorry, the correct answer was {correct_answer}.")

        # Increment the number of problems solved regardless of correctness
        problems_solved += 1
        print(f"Get ready for the next problem! {max_problems - problems_solved} to go.")

    # Final messages after all problems are completed
    print("Congratulations! You've completed the math trainer.")
    print(f'You solved {correct_counter} out of {max_problems} correctly.')

    
def subtraction_checker():
    
    print("Let's do some addition!")
    correct_counter = 0
    problems_solved = 0
    max_problems = 3  # Number of problems to solve

    while problems_solved < max_problems:
        num1, num2, oper = generate_num("-", 1, 100)  # Correct assignment order
        print(f'What is {num1} - {num2}? ')
        correct_answer = num1 - num2
        attempts = 0
        max_attempts = 3  # Number of guesses allowed

        while attempts < max_attempts:
            try:
                user_answer = float(input("Please enter an answer: "))
            except ValueError:
                print("Invalid input, please enter a valid number.")
                continue  # Continue the loop without counting the attempt

            if int(user_answer) == correct_answer:
                print("Correct! Well done!")
                correct_counter += 1
                break
            else:
                attempts += 1
                if attempts < max_attempts:
                    print(f"Incorrect. Try again. You have {max_attempts - attempts} attempts left.")

        if attempts == max_attempts:
            print(f"Sorry, the correct answer was {correct_answer}.")

        # Increment the number of problems solved regardless of correctness
        problems_solved += 1
        print(f"Get ready for the next problem! {max_problems - problems_solved} to go.")

    # Final messages after all problems are completed
    print("Congratulations! You've completed the math trainer.")
    print(f'You solved {correct_counter} out of {max_problems} correctly.') 
            

def multiplication_checker():
    
    print("Let's do some addition!")
    correct_counter = 0
    problems_solved = 0
    max_problems = 3  # Number of problems to solve

    while problems_solved < max_problems:
        num1, num2, oper = generate_num("*", 1, 100)  # Correct assignment order
        print(f'What is {num1} * {num2}? ')
        correct_answer = num1 * num2
        attempts = 0
        max_attempts = 3  # Number of guesses allowed

        while attempts < max_attempts:
            try:
                user_answer = float(input("Please enter an answer: "))
            except ValueError:
                print("Invalid input, please enter a valid number.")
                continue  # Continue the loop without counting the attempt

            if int(user_answer) == correct_answer:
                print("Correct! Well done!")
                correct_counter += 1
                break
            else:
                attempts += 1
                if attempts < max_attempts:
                    print(f"Incorrect. Try again. You have {max_attempts - attempts} attempts left.")

        if attempts == max_attempts:
            print(f"Sorry, the correct answer was {correct_answer}.")

        # Increment the number of problems solved regardless of correctness
        problems_solved += 1
        print(f"Get ready for the next problem! {max_problems - problems_solved} to go.")

    # Final messages after all problems are completed
    print("Congratulations! You've completed the math trainer.")
    print(f'You solved {correct_counter} out of {max_problems} correctly.')    
            
def division_checker():
    
    print("Lets do some addition!")
    correct_counter = 0
    problems_solved = 0
    max_problems = 3  # Number of problems to solve
       
    while problems_solved < max_problems:
        num1, num2, oper = generate_num("/", 10, 100 )
        print(f'What is {num2} / {num1}? ')
        correct_answer = round(num2 / num1, 2)  # rounding to 2 decimal places
        attempts = 0
        max_attempts = 3  # Number of guesses allowed
        while attempts < max_attempts:
           user_answer = float(input("Please enter an answer"))
    
           if user_answer is None:
               # Invalid input, prompt again without counting the attempt
               continue
    
           if round(user_answer, 2) == correct_answer:
               print("Correct! Well done!")
               correct_counter += 1
               break
           else:
               attempts += 1
               if attempts < max_attempts:
                   print(f"Incorrect. Try again. You have {max_attempts - attempts} attempts left.")
    
        if attempts == max_attempts:
           print(f"Sorry, the correct answer was {correct_answer}.")
           problems_solved += 1
    
        
           print(f"Get ready for the next problem! {max_problems - problems_solved} to go.")
        
        print("Congratulations! You've completed the math trainer.")
        print(f'You completed {correct_counter} out of {max_problems} correctly.')
choice()