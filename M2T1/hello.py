#Minimal Flask app

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # multiquote for multiline
    return """
    <h1>Hello, World!</h1>
    <p>This is a paragraph</p>
    <ol>
        <li>This</li>
        <li>is</li>
        <li>list</>
    </ol>
    <a href="action">Click me</a>
    """

@app.route("/action")

def action():
    return "Hello from the action route!"



