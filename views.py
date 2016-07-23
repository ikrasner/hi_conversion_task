from flask import render_template, flash, redirect, session, url_for, request, g

from application import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    error = None
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('loggedin'))
    username = request.form['username']
    password = request.form['password']
    #https://blog.openshift.com/use-flask-login-to-add-user-authentication-to-your-python-application/
    #registered_user = User.query.filter_by(username=username,password=password).first()
    if request.method == 'POST':
        if username != 'admin' or password != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('index.html', error=error)
