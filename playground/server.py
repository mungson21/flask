from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<int:num>')
def play_qty(num):
    return render_template('play_qty.html', num = num)

@app.route('/play/<int:num>/<color>')
def play_color(num, color):
    return render_template('color.html', num = num, color = color)

if __name__=="__main__":
    app.run(debug=True)