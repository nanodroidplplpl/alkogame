from django.shortcuts import render
from django.shortcuts import Http404
from game.models import Sesje, Gracze
import datetime, random
from django.utils import timezone

from game.models import Sesje, Gracze
from game.forms import PostScoreForm
# Create your views here.

def index(request):
    return render(request, 'game/index.html')

def room(request, ses_id):
    if request.method == 'GET':
        try:
            ses_id = str(ses_id)
            sss = Sesje.objects.get(ses_number=ses_id)
        except Sesje.DoesNotExist:
            raise Http404("Nie ma takiej sesji sory...")
        return render(request, 'game/room.html', {'sesja':sss})
    elif request.method == 'POST':
        data = Sesje.objects.get(ses_number = ses_id)
        #s = request.POST.get("score")
        #s = int(s)
        #if s < 10:
        data.gracze_set.create(g_nick=request.POST.get("g_nickk"),score=request.POST.get("scoree"))
        print(type(request.POST.get("score")))

        try:
            ses_id = str(ses_id)
            sss = Sesje.objects.get(ses_number=ses_id)
        except Sesje.DoesNotExist:
            raise Http404("Nie ma takiej sesji sory...")
        return render(request, 'game/room.html', {'sesja':sss})



def newses(request):
    what = True
    while(what == True):
        num = random.randint(100000,1000000)
        if(Sesje.objects.filter(ses_number=num)):
            what = True
        else:
            what = False
            s = Sesje(ses_number=num, end_time=timezone.now()+datetime.timedelta(days=7))

    s.save()
    return render(request, 'game/room.html', {'sesja':s})

def test_photo(request):
    return render(request, 'game/tesserac_ex.html');
