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
    file = request.form.get('file')
    n = request.form.get('n')
    if not file or not n:
        abort(400, 'Bad form data')
    block_dict = json.loads(file.read().decode('utf-8'))
    combos = blocking.test_all_combos(block_dict, n)
    return render_template('test.html', combos=combos)


if __name__ == "__main__":
    app.run()
