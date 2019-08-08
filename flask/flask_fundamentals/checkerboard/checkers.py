from flask import Flask, render_template  
app = Flask(__name__)

@app.route('/')                           
def play():
    return render_template("checkers.html", num_times=8**)

@app.route('/<num_times>')                           
def play_num(num_times):
    return render_template("checkers.html", num_times=int(num_times))

@app.route('/<x_>/<y_>')                           
def play_color(num_times, x_, y_):
    return render_template("checkers.html", num_times=int(num_times))

    
if __name__=="__main__":
    app.run(debug=True)

