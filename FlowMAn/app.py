# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:09:29 2024

@author: isbla
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session

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
        # Process the equation (same logic as your answer_checker function)
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
                        session['score'] = session.get('score', 0) + 1
                        session['current_index'] = current_index + 1
                    else:
                        session['attempts'] = session.get('attempts', 0) + 1
                        if session['attempts'] >= 3:
                            flash(f"Sorry, that's incorrect. The correct answer was {correct_answer}.")
                            session['current_index'] = current_index + 1
                            session['attempts'] = 0  # Reset attempts
                        else:
                            flash(f"Incorrect. You have {3 - session['attempts']} guesses left.")

                except ValueError:
                    flash("Please enter a valid number.")

        elif 'restart' in request.form:
            # Reset session variables for a new game
            session['current_index'] = 0
            session['attempts'] = 0
            session['score'] = 0
            return redirect(url_for('memory_bank'))

        return redirect(url_for('memory_bank'))

    # Initialize session variables if starting a new game
    if 'current_index' not in session:
        session['current_index'] = 0
        session['attempts'] = 0
        session['score'] = 0

    # Get the current question
    current_index = session['current_index']
    if current_index < len(memory):
        current_question = memory[current_index]
    else:
        # All questions answered
        final_score = session.get('score', 0)  # Use .get() to avoid KeyError
        # Reset session variables for a new game
        session['current_index'] = 0
        session['attempts'] = 0
        session['score'] = 0
        return render_template('memory_bank.html', current_question=None, final_score=final_score)

    return render_template('memory_bank.html', current_question=current_question)

if __name__ == '__main__':
    app.run(debug=True)