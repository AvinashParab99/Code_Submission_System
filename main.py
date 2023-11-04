from flask import Flask, render_template, request, send_from_directory
import os
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/problem')
def get_problem():
    with open('problem.txt', 'r') as file:
        problem = file.read()
    return problem



@app.route('/submit', methods=['POST'])
def submit_code():
    language = request.form['language']
    code = request.form['code']

    username = 'test_user'  # Replace with actual user authentication
    timestamp = int(time.time())
    problem_code = 'your_problem_code'  # Replace with an appropriate code

    if language == 'python':
        filename = f"{username}_{timestamp}_{problem_code}.py"
    elif language == 'javascript':
        filename = f"{username}_{timestamp}_{problem_code}.js"
    else:
        # Handle other languages if needed
        return "Invalid language selected!"

    submissions_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'submissions')
    file_path = os.path.join(submissions_folder, filename)

    with open(file_path, 'w') as file:
        file.write(code)

    return "Code submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)
