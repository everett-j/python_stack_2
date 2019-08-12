from flask import Flask, render_template, request, redirect, session # added request
import random
app = Flask(__name__)
app.secret_key = 'my secret' # set a secret key for security purposes
# our index route will handle rendering our form

@app.route('/')
def index():
    if 'message' not in session:
        session["message"]=""
    if 'number' not in session:
        session['number']=random.randrange(1,101)
    return render_template("index.html", message=session['message'] )

@app.route('/guess', methods=['POST'])
def guess():
    guess=int(request.form['number'])
    if guess== session['number']:
        session['message']= "YOU WON!"
    if guess > session['number']:
        session['message']= 'You guessed too High'
    elif guess< session['number']:
        session['message']= 'Too Low, Guess again.'
    return redirect('/')
@app.route('/destroy')
def destroy():
    session['number']
    session.pop("number")
    session.pop("message")
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)



