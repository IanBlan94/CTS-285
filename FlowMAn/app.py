# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:09:29 2024

@author: isbla
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session
  # Import eval for evaluation (Note: be careful with eval in production)
import random
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Global memory list
memory = [
    "1 + 1 =",
    "2 * 3 =",
    "4 - 2 =",
    "10 / 2 =",
    "5 + 7 =",
    "6 * 2 =",
    "9 / 3 =",
    "3 + 6 =",
    "7 - 4 ="
]

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/answer_checker', methods=['GET', 'POST'])
def answer_checker():
    if request.method == 'POST':
        equation = request.form['equation']
        # Process the equation
        if '=' not in equation:
            flash("Please enter an equation with '='.")
            return redirect(url_for('answer_checker'))
        
        lhs, rhs = equation.split('=')
        lhs, rhs = lhs.strip(), rhs.strip()

        # Handle division by zero and evaluate
        try:
            if '0 / 0' in lhs or '/ 0' in lhs:
                flash("Error: Division by zero is not allowed.")
                return redirect(url_for('answer_checker'))
            
            correct_answer = eval(lhs)
            user_answer = float(rhs)
            
            if abs(correct_answer - user_answer) < 1e-9:
                flash("Correct! Well done!")
            else:
                flash(f"Incorrect. The correct result for {lhs} is {correct_answer}.")
        except Exception as e:
            flash(f"Error: {str(e)}.")
        return redirect(url_for('answer_checker'))
    
    return render_template('answer_checker.html')


@app.route('/memory_bank', methods=['GET', 'POST'])
def memory_bank():
    global memory  # Reference the global memory list

    if request.method == 'POST':
        if 'add_question' in request.form:
            equation = request.form['new_equation']
            # Check if the equation contains '='
            if '=' not in equation:
                flash("Please enter an equation with '='.")
            else:
                lhs, rhs = equation.split('=')
                lhs = lhs.strip()
                rhs = rhs.strip()

                if '0 / 0' in lhs or '/ 0' in lhs:
                    flash("Error: Division by zero is not allowed. Please enter a valid equation.")
                if rhs.isdigit():
                    flash("Please enter a equation without an answer at the end")
                else:
                    try:
                        # Evaluate the left-hand side (LHS) to ensure it's a valid equation
                        correct_answer = eval(lhs)

                        # If memory is full (10 questions), remove the first question
                        if len(memory) >= 10:
                            removed_question = memory.pop(0)  # Remove the first question
                            flash(f"Removed question: {removed_question}")

                        # Add the new equation to memory
                        memory.append(equation)
                        flash("Equation added successfully!")
                    except (ValueError, SyntaxError, NameError) as e:
                        flash(f"Error: {str(e)}. Please enter a valid equation.")
                    except TypeError as e:
                        flash(f"Type Error: {str(e)}. Please ensure you're entering a valid numerical equation.")

        elif 'guess' in request.form:
            current_index = session.get('current_index', 0)
            user_answer = request.form.get('answer')

            # Check the answer
            if user_answer:
                try:
                    user_answer = float(user_answer)
                    correct_answer = eval(memory[current_index].split('=')[0])

                    if user_answer == correct_answer:
                        flash("Congrats! You solved the problem correctly!")
                        # Update score
                        session['correct_answers'] = session.get('correct_answers', 0) + 1
                        session['attempts'] = 0
                        # Move to the next question
                        session['current_index'] = current_index + 1
                        
                    else:
                        session['attempts'] = session.get('attempts', 0) + 1
                        if session['attempts'] >= 3:
                            flash(f"Sorry, that's incorrect. The correct answer was {correct_answer}.")
                            # Move to the next question
                            session['current_index'] = current_index + 1
                            session['attempts'] = 0  # Reset attempts
                        else:
                            flash(f"Incorrect. You have {3 - session['attempts']} guesses left.")

                except ValueError:
                    flash("Please enter a valid number.")

        return redirect(url_for('memory_bank'))

    # Initialize session variables if starting a new game
    if 'current_index' not in session:
        session['current_index'] = 0
        session['attempts'] = 0
        session['correct_answers'] = 0

    # Get the current question
    current_index = session['current_index']
    if current_index < len(memory):
        current_question = memory[current_index]
        final_score = None
    else:
        current_question = None  # No more questions left
        final_score = session.get('correct_answers', 0)  # Retrieve final score from session

    # Render the memory bank page with the current question
    return render_template('memory_bank.html', memory=memory, current_question=current_question, final_score=final_score)

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:09:29 2024

@author: isbla
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session
  # Import eval for evaluation (Note: be careful with eval in production)
import random
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Global memory list
memory = [
    "1 + 1 =",
    "2 * 3 =",
    "4 - 2 =",
    "10 / 2 =",
    "5 + 7 =",
    "6 * 2 =",
    "9 / 3 =",
    "3 + 6 =",
    "7 - 4 ="
]

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/answer_checker', methods=['GET', 'POST'])
def answer_checker():
    if request.method == 'POST':
        equation = request.form['equation']
        # Process the equation
        if '=' not in equation:
            flash("Please enter an equation with '='.")
            return redirect(url_for('answer_checker'))
        
        lhs, rhs = equation.split('=')
        lhs, rhs = lhs.strip(), rhs.strip()

        # Handle division by zero and evaluate
        try:
            if '0 / 0' in lhs or '/ 0' in lhs:
                flash("Error: Division by zero is not allowed.")
                return redirect(url_for('answer_checker'))
            
            correct_answer = eval(lhs)
            user_answer = float(rhs)
            
            if abs(correct_answer - user_answer) < 1e-9:
                flash("Correct! Well done!")
            else:
                flash(f"Incorrect. The correct result for {lhs} is {correct_answer}.")
        except Exception as e:
            flash(f"Error: {str(e)}.")
        return redirect(url_for('answer_checker'))
    
    return render_template('answer_checker.html')


@app.route('/memory_bank', methods=['GET', 'POST'])
def memory_bank():
    global memory  # Reference the global memory list

    if request.method == 'POST':
        if 'add_question' in request.form:
            equation = request.form['new_equation']
            # Check if the equation contains '='
            if '=' not in equation:
                flash("Please enter an equation with '='.")
            else:
                lhs, rhs = equation.split('=')
                lhs = lhs.strip()
                rhs = rhs.strip()

                if '0 / 0' in lhs or '/ 0' in lhs:
                    flash("Error: Division by zero is not allowed. Please enter a valid equation.")
                if rhs.isdigit():
                    flash("Please enter a equation without an answer at the end")
                else:
                    try:
                        # Evaluate the left-hand side (LHS) to ensure it's a valid equation
                        correct_answer = eval(lhs)

                        # If memory is full (10 questions), remove the first question
                        if len(memory) >= 10:
                            removed_question = memory.pop(0)  # Remove the first question
                            flash(f"Removed question: {removed_question}")

                        # Add the new equation to memory
                        memory.append(equation)
                        flash("Equation added successfully!")
                    except (ValueError, SyntaxError, NameError) as e:
                        flash(f"Error: {str(e)}. Please enter a valid equation.")
                    except TypeError as e:
                        flash(f"Type Error: {str(e)}. Please ensure you're entering a valid numerical equation.")

        elif 'guess' in request.form:
            current_index = session.get('current_index', 0)
            user_answer = request.form.get('answer')

            # Check the answer
            if user_answer:
                try:
                    user_answer = float(user_answer)
                    correct_answer = eval(memory[current_index].split('=')[0])

                    if user_answer == correct_answer:
                        flash("Congrats! You solved the problem correctly!")
                        # Update score
                        session['correct_answers'] = session.get('correct_answers', 0) + 1
                        session['attempts'] = 0
                        # Move to the next question
                        session['current_index'] = current_index + 1
                        
                    else:
                        session['attempts'] = session.get('attempts', 0) + 1
                        if session['attempts'] >= 3:
                            flash(f"Sorry, that's incorrect. The correct answer was {correct_answer}.")
                            # Move to the next question
                            session['current_index'] = current_index + 1
                            session['attempts'] = 0  # Reset attempts
                        else:
                            flash(f"Incorrect. You have {3 - session['attempts']} guesses left.")

                except ValueError:
                    flash("Please enter a valid number.")

        return redirect(url_for('memory_bank'))

    # Initialize session variables if starting a new game
    if 'current_index' not in session:
        session['current_index'] = 0
        session['attempts'] = 0
        session['correct_answers'] = 0

    # Get the current question
    current_index = session['current_index']
    if current_index < len(memory):
        current_question = memory[current_index]
        final_score = None
    else:
        current_question = None  # No more questions left
        final_score = session.get('correct_answers', 0)  # Retrieve final score from session

    # Render the memory bank page with the current question
    return render_template('memory_bank.html', memory=memory, current_question=current_question, final_score=final_score)

@app.route('/guesser_game', methods=['GET', 'POST'])
def guesser_game():
    if 'num' not in session:  # Generate random number and reset counter if not already set
        session['num'] = random.randint(1, 100)
        session['counter'] = 0
        session['game_over'] = False  # Add a flag to indicate if the game is over

    message = "Welcome to the guessing game! Try to guess a number between 1 and 100 in 3 tries!"

    if session['num'] > 50:
        hint = ("Beyond the middle, I start to climb, "
                "To greater heights in a short time, "
                "Can you find me where the numbers shine?")
    else:
        hint = ("In the lower fields where shadows play, "
                "I rest where modest numbers stay, "
                "A hint of the middle, but I don’t sway.")

    if request.method == 'POST' and not session['game_over']:
        try:
            guess = int(request.form['guess'])  # User input

            session['counter'] += 1  # Increment attempt counter

            if guess == session['num']:
                message = f"Congrats! You've won in {session['counter']} tries! The correct number was {session['num']}"
                session['game_over'] = True  # Set game over to True
            elif session['counter'] >= 3:
                message = f"Sorry, you've used all 3 tries! The correct number was {session['num']}."
                session['game_over'] = True  # Set game over to True
            else:
                message = "Please try again."
                if guess < session['num']:
                    message = f"Alittle taller and you may just reach!"
                else:
                    message = f"Maybe try ducking a little lower to get there"

        except ValueError:
            flash("Please enter a valid number.")

    return render_template('guesser_game.html', message=message, hint=hint, game_over=session['game_over'])

@app.route('/reset_game')
def reset_game():
    session.pop('num', None)  # Reset the number
    session.pop('counter', None)  # Reset the counter
    session.pop('game_over', None)  # Reset game over flag
    return redirect(url_for('guesser_game'))

    
    
if __name__ == '__main__':
    app.run(debug=True)
