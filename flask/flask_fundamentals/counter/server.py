from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
app.secret_key = 'my secret' # set a secret key for security purposes
# our index route will handle rendering our form
app.count = 0

@app.route('/')
def index():
    if "count" not in session:
        session["count"]=1
    session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/add', methods=['POST'])
def add():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy', methods=['POST'])
def destroy():
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)



