from flask import Flask  
app = Flask(__name__)    
#KEEP THIS CODE ABOVE 

@app.route('/')     
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def success():
    return 'Dojo!'
    
@app.route('/say/<name>')
def hello(name):
    return (f"Hi  {name} !")

@app.route('/repeat/<rep>/<phrase>')
def repeater(phrase, rep):
    rep = int(rep)
    return(f"{phrase}\n" * rep)

@app.route("/<name>/<times>")
def hello_person(name, times)
    print(name)
    return render_template
    ("play.html".
    some_name=name,
    num_times=int(times))





#KEEP THIS CODE BELOW 
if __name__=="__main__":
    app.run(debug=True)


