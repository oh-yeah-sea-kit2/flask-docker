import firebase_admin
import flask
from firebase_admin import firestore
from flask import request

app = flask.Flask(__name__)

firebase_admin.initialize_app()
SUPERHEROES = firestore.client().collection('superheroes')


@app.route('/', methods=['GET'])
def index():
    return """
    <h1> Create hero? </h1>
    <form method="post" action='/heroes'>
        <input type="text" size="30" name="hero name">
        <input type="submit" value="create hero">
    </form>
    <h1> Read hero? </h1> 
    <form method="post" action='/read'>
        <input type="text" size="30"name="id">
        <input type="submit" value="read hero">
    </form> 
    """


@app.route('/heroes', methods=['POST'])
def create_hero():
    req = {"name": request.form['hero name']}
    hero = SUPERHEROES.document()
    hero.set(req)
    return """
    <h1> id': %s </h1>
    <form method="get" action='/'>
        <input type="submit" size="30" value="back to the index">
    </form>
    """ % hero.id


@app.route('/read', methods=['POST'])
def read_hero():
    id = request.form['id']
    heroname = _ensure_hero(id).to_dict()
    return """
    <h1> hero is %s </h1>
    <form method="get" action='/'>
        <input type="submit" value="back to the index">
    </form>
    """ % heroname['name']


def _ensure_hero(id):
    try:
        return SUPERHEROES.document(id).get()
    except:
        flask.abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

