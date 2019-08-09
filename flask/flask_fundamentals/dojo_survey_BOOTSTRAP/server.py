from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

           
@app.route('/process', methods=['POST'])
def create_user():
    print("Submitted Info")
    print(request.form)
    session['full_name'] = request.form['full_name_form']
    session['dojo_location'] = request.form['dojo_location_form']
    session['fav_language'] = request.form['fav_language_form']
    session['comments'] = request.form['comments_form']
    return redirect("/response")

@app.route('/response')
def show_user():
    return render_template('response.html', full_name_on_template=session['full_name'], fav_language_on_template=session['fav_language'], dojo_location_on_template=session['dojo_location'], comments_on_template=session['comments'])



if __name__ == "__main__":
    app.run(debug=True)



