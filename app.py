from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add')
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify(result=a + b)

@app.route('/subtract')
def subtract():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify(result=a - b)

@app.route('/multiply')
def multiply():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify(result=a * b)

@app.route('/divide')
def divide():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 1))  # Avoid divide by zero
    if b == 0:
        return jsonify(error="Cannot divide by zero"), 400
    return jsonify(result=a / b)

if __name__ == '__main__':
    app.run(debug=True)
