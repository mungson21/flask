from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'key_name'

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html')

@app.route('/destory_session')
def destory_session():
    session.clear()
    return redirect('/')

# @app.route('/test')
# def test():
#     return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)