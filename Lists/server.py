from flask import Flask, render_template
app = Flask(__name__)

@app.route('/lists')
def lists():
    student_info = [
        {'name': 'Ryan', 'age': 24},
        {'name': 'George', 'age': 49},
        {'name': 'Benjamin', 'age': 63}
    ]
    return render_template('lists.html', numbers = [1,3,5,7,9], students = student_info)

if __name__ == "__main__":
    app.run(debug=True)
