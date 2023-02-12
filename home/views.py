from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world! William Andrew Turner is a dumb monkey")
def front_page(request):
    return render(request, 'hello.html')
# Create your views here. It is a Request Handler
