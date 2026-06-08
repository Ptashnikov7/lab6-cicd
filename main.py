import os
from flask import Flask, request, jsonify

# Модель: Метод Ньютона (5 семестр)
# Автор: Пташников Василь, група АІ-235

app = Flask(__name__)

def f(x):
    return x**2 - 2

def f_prime(x):
    return 2*x

def newton_method(x0, eps=0.0001):
    x = x0
    for _ in range(1000):
        if f_prime(x) == 0:
            return None
        x_next = x - f(x)/f_prime(x)
        if abs(x_next - x) < eps:
            return x_next
        x = x_next
    return x

@app.route('/calculate', methods=['GET'])
def calculate():
    x_param = request.args.get('x', default='1.0')
    try:
        x0 = float(x_param)
        root = newton_method(x0)
        if root is None:
            return jsonify({"error": "Method did not converge"}), 400
            
        return jsonify({
            "model": "Newton Method",
            "student": "Ptashnikov Vasyl",
            "group": "AI-235",
            "input_x0": x0,
            "result_root": root
        })
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
