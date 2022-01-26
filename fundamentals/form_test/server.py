from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

# [('name', 'Michael'),
# ('email', 'ungson001@live.com')]

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Before session:
        # print(request.form)
        # name = request.form['name']
        # email = request.form['email']

    # Implementing Session:
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")

# adding this method
@app.route("/show")
def show_user():
    # Before Session:
        # print("Showing the User Info From the Form")
        # print(request.form)
        # return render_template("show.html")

    # After session in server.py file
    # return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

    # Session redirected in html file:
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)