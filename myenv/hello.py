from flask import Flask # type: ignore
from flask import url_for # type: ignore
from flask import session
from flask import request
from flask import redirect
app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return "Page does not exist"
    


