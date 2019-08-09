from flask import Flask, render_template, request, redirect # added request
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

           
@app.route('/response', methods=['POST'])
def create_user():
    print("Submitted Info")
    print(request.form)
    full_name_from_form = request.form['full_name']
    location_from_form = request.form['dojo_location']
    fav_language_from_form = request.form['fav_language']
    comments_from_form = request.form['comments']
    return render_template("response.html", full_name_on_template=full_name_from_form, fav_language_on_template=fav_language_from_form, location_on_template=location_from_form, comments_on_template=comments_from_form)

def return_butt():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)



