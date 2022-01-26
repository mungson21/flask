from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def index():
    return render_template('index.html')

# [('player1_name', 'Mike'),
#  ('player1_move', 'Rock'),
#  ('player2_name', 'Rob'),
#  ('plyaer2_move', 'Rock')]

@app.route('/process_form', methods=['POST'])
def process_form():
    session['data']=request.form

    return redirect('/result')

@app.route('/result')
def result():
    result=''

    player1Move=session['data']['player1_move']
    player2Move=session['data']['player2_move']

    if player1Move == 'rock' and player2Move == 'scisccors':
        result='Player 1 Wins'
    elif player1Move == 'scissors' and player2Move == 'rock':
        result='Player 2 Wins'
    elif player1Move == player2Move:
        result='Tie'

    return render_template('results.html', player1_name=session['data']['player1_name'], player2_name=session['data']['player2_name'], result=result)

if __name__ == "__main__":
    app.run(debug=True)