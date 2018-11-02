from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt


# Create your views here.
def index(request):

    return render(request,'index.html')

def today_photos(request):
    date=dt.date.today()


    return render(request,'all-photos/today-photos.html',{"date":date})


def past_photos(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

    if date == dt.date.today():
        return redirect(today_photos)
    return render(request,'all-photos/past-photos.html',{"date":date})
