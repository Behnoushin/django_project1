from django.http import HttpResponse

def index (request):
    #body
    return HttpResponse('Welcome to Django')
