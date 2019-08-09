from flask import Flask, render_template  
app = Flask(__name__)

@app.route('/')                           
def checkers():
    return render_template("checkers.html", r1=8, r2=8)

@app.route('/<r1>')
def checkers_x(r1):
    return render_template("checkers.html", r1=int(r1), r2=8)

@app.route('/<r1>/<r2>')
def checkers_y(r1,r2):
    return render_template("checkers.html", r1=int(r1), r2=int(r2))



    
if __name__=="__main__":
    app.run(debug=True)


