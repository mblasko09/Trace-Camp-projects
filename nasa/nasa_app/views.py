from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
from django.utils.dateparse import parse_date
from nasa_app.models import NasaComment

def comment_create(request):
    if (request.method == 'GET'):
        api_key = "oMrH77hL0IcYFpEAYw6HpzxULiro2VX2jGy9CIMV"
        date = request.get.GET("date")
        r = request.get(f'https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}')
        url = r.json()["url"]
        return render(request, 'create_comment.html', {"nasa_url": url, "date": date})

    elif (request.method == 'POST'):
        nasa_comment = NasaComment.objects.create(
            comment = request.POST.get('comment'),
            rating = request.POST.get('rating'),
            date = request.POST.get('date'),
            )
        return redirect('nasa/comment/' + str(nasa_comment.id))

def comment(request):
    nasa_comment = NasaComment.objects.get(id = nasa_id)
    return render(request, 'comments.html', {"comment" : comment})

def comment_list(request):
    nasa_comment_list = NasaComment.objects.all()
    return render(request, 'comment_list.html', {"nasa_comment" : nasa_comment})

def date_pick(request):
    if (request.method == 'POST'):
        date = request.POST.get('date')
        return redirect('nasa/comment/create/?date=' + date)
    elif (request.method == 'GET'):
        return render(request, 'date_picker.html', {})
