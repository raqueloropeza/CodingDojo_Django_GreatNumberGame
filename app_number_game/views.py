from django.shortcuts import render, redirect
import random

def index(request):
    #Check to see if random is stored in session.  If not, then clear message and generate a random number between 1 and 100 to be stored in session.
    if 'random' not in request.session:
        request.session['message']= ""
        request.session['random'] = random.randrange(1,101)
        print(request.session['random'])
    return render(request,"index.html")

def guess(request):
    #If input from form (guess) equals integer in session, have the message display "Correct".
    if request.session['random'] == int(request.POST['guess']):
        request.session['message'] = "correct"
    #If input from form (guess) is greater than integer in session, have the message display "High".
    if request.session['random'] < int(request.POST['guess']):
        request.session['message'] = "high"
    #If input from form (guess) is lower than integer in session, have the message display "Low".
    elif request.session['random'] > int(request.POST['guess']):
        request.session['message'] = "low"
    return render(request, "index.html")

def reset(request):
    #Have route clear session. 
    del request.session['message']
    del request.session['random']
    return redirect("/")





