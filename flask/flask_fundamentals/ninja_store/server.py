from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    raspberry_from_form = request.form['raspberry']
    strawberry_from_form = request.form['strawberry']
    apple_from_form = request.form['apple']
    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    student_id_from_form = request.form['student_id']
    return render_template("checkout.html", raspberry_on_template=raspberry_from_form, strawberry_on_template=strawberry_from_form, apple_on_template=apple_from_form, first_name_on_template=first_name_from_form, last_name_on_template=last_name_from_form, student_id_on_template=student_id_from_form)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    