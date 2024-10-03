# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:09:29 2024

@author: isbla
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import eval  # Import eval for evaluation (Note: be careful with eval in production)

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
    if request.method == 'POST':
        if 'add_question' in request.form:
            equation = request.form['new_equation']
            if len(memory) < 10:
                memory.append(equation)
                flash("Equation added successfully!")
            else:
                flash("Memory full! Remove a question before adding more.")
        elif 'practice' in request.form:
            # Implement practice logic here if needed
            pass
        return redirect(url_for('memory_bank'))
    
    return render_template('memory_bank.html', memory=memory)

if __name__ == '__main__':
    app.run(debug=True)