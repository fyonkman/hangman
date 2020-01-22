##@Fiona Yonkman 2019
##App file acts as the controller between the model and views

from flask import (Flask, request, render_template, make_response,
                    redirect, url_for, session)
from model import Model

app = Flask(__name__)
m = Model()
#keeps track of wins and losses across sessions
stats = [0,0]
app.secret_key='very secret'

#route for initial start page
@app.route('/', methods=['GET','POST'])
def index():
    #clear wins and losses after return to main menu
    stats[0] = 0
    stats[1] = 0
    if request.method == "POST":
        #redirect based on difficulty button selected
        if request.form['submit'] == 'easy':
            difficulty='short'
            session['difficulty'] =difficulty
            return redirect(url_for('game', difficulty=difficulty))
        elif request.form['submit'] == 'medium':
            difficulty='medium'
            session['difficulty'] =difficulty
            return redirect(url_for('game', difficulty=difficulty))
        elif request.form['submit'] == 'hard':
            difficulty='long'
            session['difficulty'] =difficulty
            return redirect(url_for('game', difficulty=difficulty))
        else:
            print('elseelse')
            return None
        return render_template('index.html')
    else:
        return render_template('index.html')

#route that handles intermediate game states
@app.route('/game/', methods=["POST"])
def process_text():
    #If 'Try Letter' button is pressed
    if request.form['submit'] == 'btn1':
        text = request.form.get('textbox')
        m.testLetter(text)
        #if the user has won
        if len(m.correctLetters) == m.numLetters:
            m.gameState = -1
            stats[0] += 1
        kwargs = {"gameState": m.gameState, "lett": m.correctLetters,
                    "numL": m.numLetters, "ind": m.indices, "wl": stats}
        #if the user has lost
        if m.gameState >= 10:
             stats[1] += 1
             kwargs["word"] = m.word
        if not m.errortext:
            r = make_response(render_template('game.html', **kwargs))
            r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            return r
        else:
            r = make_response(render_template('game.html',
                                            **kwargs, text=str(m.errortext)))
            r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            return r
    #if 'Play Again' button is pressed, route to initial game page
    elif request.form['submit'] == 'btn2':
        return game()
    #if 'Main Menu' button is pressed, route to initial index page
    elif request.form['submit'] == 'btn3':
        return redirect(url_for('index'))
    else:
        return None

#route for game page which resets Model attributes for new game
@app.route('/game/')
def game():
    difficulty = request.args['difficulty']
    difficulty=session['difficulty']
    m.generateWord(difficulty)
    m.correctLetters = []
    m.indices = []
    m.wrongLetters=[]
    m.gameState = 0
    kwargs = {"gameState": m.gameState, "lett": m.correctLetters,
                "numL": m.numLetters, "ind": m.indices, "wl": stats}
    r = make_response(render_template('game.html', **kwargs))
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return r

#route to prevent form submission forward
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
