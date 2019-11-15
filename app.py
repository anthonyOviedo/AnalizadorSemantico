from motor.reader import initScan, symbolType


from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def hom():
    return render_template('home.html')


@app.route('/run', methods=['GET'])
def run():
    lines, errores, table = initScan()
    rows = []
    for t in table:
        obj = table[t]
        rows.append(obj.description())

    return jsonify({"lines": lines, "errors": errores, "table": rows})


if __name__ == '__main__':
    app.run(debug=True)


# print(Results)
