import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def main(request):
    now = datetime.datetime.now()
    context = {
        'userName': '軒',
        'now': now
    }

    # return HttpResponse('Test this is main home')
    return  render(request, 'main/main.html', context)

def about(request):

    return render(request, 'main/about.html')