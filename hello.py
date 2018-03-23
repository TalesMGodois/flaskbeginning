
import os

from flask import Flask, url_for, request, abort, jsonify, render_template

app = Flask(__name__)

@app.route('/chacal')
@app.route('/chacal/<test>', methods=['GET'])
def index(test = None):
    # import pdb; pdb.set_trace()
    return render_template("index.html", test_t=test)


@app.route('/testme', methods=['POST'])
def test_get():
    if request.method == 'POST':
        return jsonify(request.get_json())

    else:
        return "goturl"


@app.route("/user/<username>")
def show_user_profile(username):
    return 'this is the user: ' + username


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return post_id


# @app.before_request
# def only_json():
#     if not request.is_json:
#         abort(400)


if __name__ == '__main__':
    host = os.getenv("IP", "0.0.0.0")
    port = int(os.getenv("PORT", 3000))
    app.debug = True
    app.run(host=host, port=port)