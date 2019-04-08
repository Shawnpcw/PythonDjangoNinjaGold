from django.shortcuts import render, HttpResponse, redirect
import random, datetime
  # the index function is called when root is visited
def index(request):
    if 'totalGold' not in request.session:
        request.session['totalGold'] = 0
    return render(request, 'ninja_gold/index.html')
def process(request):
    if 'messages' not in request.session:
        request.session['messages'] =[]
   
   
    if request.POST['name'] == 'farm':
        randomnum = random.randrange(10,20)
        request.session['totalGold'] += randomnum
        request.session['messages'].append('<p class="text-success">Earned '+str(randomnum)+' golds from the farm! ('+str(datetime.datetime.now().strftime('%I:%M %p'))+')</p>')
        request.session['messages'].append('success')

    elif request.POST['name'] == 'cave':
        randomnum = random.randrange(5,10)
        request.session['totalGold'] += randomnum
        request.session['messages'].append('<p class="text-success">Earned '+str(randomnum)+' golds from the cave! ('+str(datetime.datetime.now().strftime('%I:%M %p'))+')</p>')
        request.session['messages'].append('success')

    elif request.POST['name'] == 'house':
        randomnum = random.randrange(2,5)
        request.session['totalGold'] += randomnum
        request.session['messages'].append('<p class="text-success">Earned '+str(randomnum)+' golds from the house! ('+str(datetime.datetime.now().strftime('%I:%M %p'))+')</p>')
        request.session['messages'].append('success')
    elif request.POST['name'] == 'casino':
        randomnum =random.randrange(-50,50)
        request.session['totalGold'] +=randomnum
        if randomnum > 0:
            request.session['messages'].append('<p class="text-success">Earned '+str(randomnum)+' golds from the casino! ('+str(datetime.datetime.now().strftime('%I:%M %p'))+')</p>')
            request.session['messages'].append('success')

        elif randomnum <= 0:
            randomnum = abs(randomnum)
            request.session['messages'].append('<p class="text-danger">Entered a casino and lost '+str(randomnum)+' golds... Ouch.. ('+str(datetime.datetime.now().strftime('%I:%M %p'))+')</p>')
            request.session['messages'].append('success')

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')