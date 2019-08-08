from flask import Flask, render_template  
app = Flask(__name__)

@app.route('/play')                           
def play():
    return render_template("play.html", num_times=3)

@app.route('/play/<num_times>')                           
def play_num(num_times):
    return render_template("play.html", num_times=int(num_times), color_input="blue")

@app.route('/play/<num_times>/<color_input>')                           
def play_color(num_times, color_input):
    return render_template("play.html", num_times=int(num_times), color_input=color_input)

    
if __name__=="__main__":
    app.run(debug=True)

