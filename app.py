from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Пивет!"
    )


@app.route("/info")
def info():
    return (
        "ФИО: Гайкалов Денис Александрович<br>"
        "Группа: ДССА-50<br>"
        "Дисциплина: Основы алгоритмизации и программирования"
    )


@app.route("/hello/<name>")
def hello(name):
    return f"Салам, {name}!"


@app.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    return jsonify({"a": a, "b": b, "result": a * b})


@app.route("/check/<int:number>")
def check(number):
    parity = "чётное" if number % 2 == 0 else "нечётное"
    return jsonify({"number": number, "parity": parity})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7174, debug=True)
