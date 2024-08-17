from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        operation = request.form['op']
        try:
            output = eval(operation, {"__builtins__": None}, {})
        except Exception as e:
            output = 'Error'
    else:
        output = ''

    return render_template('home.html', output=output)


if __name__ == '__main__':
    app.run(debug=True)

