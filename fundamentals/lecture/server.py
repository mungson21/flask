from flask import Flask, render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return 'Python is running'  # Return the string 'Hello World!' as a response

@app.route('/dessert')
def apple_pie():
    return 'Apple pie is bussin'

@app.route('/dessert/<name>')
def dessert(name):
    return f'{name.capitalize()} is bussin'

@app.route('/person/<first_name>') #By default this is a string
def person(first_name):
    return f'Welcome {first_name.capitalize()} to Today'

@app.route('/dessert/<int:x>/<int:y>')
def dessert_count(x, y):
    sum = x + y
    return str(sum)

@app.route('/pie_list')
def pie_list():
    return render_template('index.html', num = 5)

@app.route('/pie_list/<int:num>')
def pie_qty(num):
    return render_template('index.html', num = num)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.