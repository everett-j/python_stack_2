from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')                           
def hello_world():
    return render_template("index.html", phrase="hello", times=5)
    
@app.route('/success')
def success():
    return 'Success!'

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

