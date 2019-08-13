from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import random

def index(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
    try:
        request.session['activity']
    except KeyError:
        request.session['activity'] = []
    
    return render(request, "ninja2/index.html")

def randomNum(start, end):
    num = random.randrange(start, end)
    return num

def makeGold():
    chance = randomNum(0, 2)
    if chance == 1:
        return True
    else:
        return False

def addActivity(request, num, action, location):
    timestamp = strftime("%H : %M", gmtime())
    if location == 'casino':
        if action == 'earned':
            earned = 'Earned %d from the casino! %s' % (num, timestamp)
            request.session['activity'].append(['earn', earned])
        elif action == 'lost':
            lost = 'The Casino took %d gold. Too bad. %s' % (num, timestamp)
            request.session['activity'].append(['lost', lost])
        else:
            print("help me, errors gone wild")
    elif location == 'farm':
        request.session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    elif location == 'cave':
        request.session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    elif location == 'house':
        request.session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    else:
        print("help me, errors gone wild")

def calculateMoney(request):
    hiddenInput = request.POST["hidden"]
    if hiddenInput == 'farm':
        farmNum = randomNum(10, 21)
        request.session['gold'] += farmNum
        addActivity(request,farmNum, 'earned', 'farm')
    elif hiddenInput == 'cave':
        caveNum = randomNum(5, 10)
        request.session['gold'] += caveNum
        addActivity(request,caveNum, 'earned', 'cave')
    elif hiddenInput == 'house':
        houseNum = randomNum(2, 5)
        request.session['gold'] += houseNum
        addActivity(request,houseNum, 'earned', 'house')
    elif hiddenInput == 'casino':
        casinoNum = randomNum(0, 50)
        chance = makeGold()
        if chance == True:
            request.session['gold'] += casinoNum
            addActivity(request,casinoNum, 'earned', 'casino')
        elif chance == False:
            request.session['gold'] -= casinoNum
            addActivity(request,casinoNum, 'lost', 'casino')
        else:
            print("help me, errors gone wild")
    else:
        print("help me, errors gone wild")
    return redirect('/')

def clear(request):
    request.session['gold'] = 0
    request.session['activity'] = []
    return redirect('/')