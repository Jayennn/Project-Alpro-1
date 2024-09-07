from flask import Flask, Blueprint, request
from belajar.response import success_response, error_response
from belajar.utils import read_file
import random
app = Flask(__name__)
v1 = Blueprint('prefix', __name__, url_prefix='/api/v1')

@app.route('/', methods=['GET'])
def index():
    return success_response('Hello World!')

@v1.route('/', methods=['GET'])
def index():
    return success_response('Hello World!')

@v1.route('/khodam', methods=['GET'])
def get_khodam():
    name = request.args.get('name')
    khodam = read_file("lists.txt")

    if not khodam:
        return

    if not name:
        error_response("Name cannot be empty.", 400)
        return

    if len(khodam) == 0:
        error_response("No khodam available.", 404)

    result = khodam[random.randint(0, len(khodam) - 1)]
    return success_response({
        "nama": name,
        "khodam": result
    })

app.register_blueprint(v1)

if __name__ == '__main__':
    app.run(debug=True)