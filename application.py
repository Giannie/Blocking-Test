from flask import Flask, abort, render_template, request
import json

import blocking


# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def test():
    n = request.form.get('length')
    try:
        file = request.files['file']
    except Exception:
        file = request.form.get('json-text')
        if not file:
            abort(400, 'Missing json file')
    try:
        if type(file) == str:
            block_dict = json.loads(file)
        else:
            block_dict = json.loads(file.read().decode('utf-8'))
    except json.decoder.JSONDecodeError:
        abort(400, 'Bad json file')
    if not n:
        n = 4
    else:
        try:
            n = int(n)
        except ValueError:
            abort(400, "bad number entry")
    combos = []
    for i in range(2, n + 1):
        new_combos = blocking.test_all_combos(block_dict, i)
        for combo in new_combos:
            if not blocking.is_dependent_combo(combo, combos):
                combos.append(combo)
    json_list = [",".join(combo) for combo in combos]
    return render_template('test.html', combos=combos,
                           json_list=str(json_list))


if __name__ == "__main__":
    app.run()
