from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')