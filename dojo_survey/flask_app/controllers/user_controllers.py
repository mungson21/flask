from flask_app import app

from flask import render_template, request, redirect, session

from flask_app.models.user_model import User


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['data']=request.form
    form_data = {
        'name' : request.form['name'],
        'location' : request.form['location'],
        'language' : request.form['language'],
        'comment' : request.form['comment']
    }
    valid = User.user_validation(form_data)
    if valid:
        results = User.create_user(form_data)
        return redirect(f'/results/{results}')
    return redirect('/')

@app.route('/results/<int:user_id>')
def get_one(user_id):
    data = {
        'id' : user_id
    }
    user = User.get_one(data)
    return render_template('results.html', user=user, name=session['data']['name'], location=session['data']['location'], language=session['data']['language'], comment=session['data']['comment'])

