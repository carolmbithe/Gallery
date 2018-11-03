from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image,Location


# Create your views here.
def index(request):

    photos=Image.get_photos()

    return render(request,'index.html',{"photos":photos})

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


def location(request,location_id):
    photos=Image.objects.filter(id=location_id)

    return render(request,'location.html',{"photos":photos})

def category(request,category_id):
    image=Image.objects.filter(id=category_id)

    return render(request,'category.html',{"image":image})


def image(request,image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
         raise Http404()
    return render(request,"image.html",{"image":image})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})
