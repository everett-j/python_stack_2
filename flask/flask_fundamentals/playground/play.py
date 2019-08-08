from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')                           
def play():
    return render_template("play.html", phrase="hello", times=5)
    
@app.route("/<name>/<times>")
def hello_person(name, times):
    print(name)
    return render_template("name.html",some_name=name,num_times=int(times))

    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

