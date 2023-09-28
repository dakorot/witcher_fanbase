from django.template import loader
from django.http import HttpResponse


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def top(request):
    template = loader.get_template('top.html')
    return HttpResponse(template.render())

def latest(request):
    template = loader.get_template('latest.html')
    return HttpResponse(template.render())
