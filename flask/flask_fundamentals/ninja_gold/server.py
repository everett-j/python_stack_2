from flask import Flask, render_template, request, redirect, session # added request
import random
import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form
def randomNum(start, end):
    num = random.randrange(start, end)
    return num

def makeGold():
    chance = randomNum(0, 2)
    if chance == 1:
        return True
    else:
        return False

def addActivity(num, action, location):
    timestamp = datetime.datetime.now()
    if location == 'casino':
        if action == 'earned':
            earned = 'Earned %d from the casino! %s' % (num, timestamp)
            session['activity'].append(['earn', earned])
        elif action == 'lost':
            lost = 'The Casino took %d gold. Too bad. %s' % (num, timestamp)
            session['activity'].append(['lost', lost])
        else:
            print("help me, errors gone wild")
    elif location == 'farm':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    elif location == 'cave':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    elif location == 'house':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    else:
        print("help me, errors gone wild")

@app.route('/')
def index():
    try:
        session['gold']
    except KeyError:
        session['gold'] = 0
    try:
        session['activity']
    except KeyError:
        session['activity'] = []
    return render_template('index.html', gold=session['gold'], activities=session['activity'])

@app.route('/process_money', methods=['POST'])
def calculateMoney():
    hiddenInput = request.form['hidden']
    if hiddenInput == 'farm':
        farmNum = randomNum(10, 21)
        session['gold'] += farmNum
        addActivity(farmNum, 'earned', 'farm')
    elif hiddenInput == 'cave':
        caveNum = randomNum(5, 10)
        session['gold'] += caveNum
        addActivity(caveNum, 'earned', 'cave')
    elif hiddenInput == 'house':
        houseNum = randomNum(2, 5)
        session['gold'] += houseNum
        addActivity(houseNum, 'earned', 'house')
    elif hiddenInput == 'casino':
        casinoNum = randomNum(0, 50)
        chance = makeGold()
        if chance == True:
            session['gold'] += casinoNum
            addActivity(casinoNum, 'earned', 'casino')
        elif chance == False:
            session['gold'] -= casinoNum
            addActivity(casinoNum, 'lost', 'casino')
        else:
            print("help me, errors gone wild")
    else:
        print("help me, errors gone wild")
    return redirect('/')



@app.route('/clear', methods=['POST'])
def clear():
    session['gold'] = 0
    session['activity'] = []
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)



