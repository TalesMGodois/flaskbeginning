import os

from flask import Flask, url_for, request, abort, jsonify, render_template, redirect, flash

app = Flask(__name__)


@app.route('/', endpoint='start')
@app.route('/login', methods=['POST'])
def login():
    error = None
    retorno = render_template('login.html')
    if request.method == 'POST':
        user = request.values['user']
        hash_pass = request.values['hashPass']

        if valid_login(user, hash_pass):
            flash("succesfully logged in")
            retorno =  redirect(url_for('index', test=user))
        else:
            flash('Incorrect user and password')
            retorno = redirect(url_for('start'))

    return retorno




@app.route('/chacal/<test>')
def index(test=None):
    # import pdb; pdb.set_trace()
    return render_template("index.html", test_t=test)


def valid_login(user,password):
    return user == password

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


def start():
    if __name__ == '__main__':
        host = os.getenv("IP", "0.0.0.0")
        port = int(os.getenv("PORT", 3000))
        app.debug = True
        app.secret_key = "xablau"
        app.run(host=host, port=port)

start()
