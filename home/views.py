from django.shortcuts import render
import africastalking 
from  django.http  import HttpResponse
from django.views.decorators.csrf import csrf_exempt
username = "tuganimana01@gmail.com"    # use 'sandbox' for development in the test environment
api_key = "5f27a189e04ed8e077e10702682a2719c9e2470e56076c1a7b5899250cd4ceaf"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)

# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@csrf_exempt
def ussdapp(request):

    if request.method == 'POST':
        ## mandatory
        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST.get("text")
        level = text.split('*')
        response =""

        if text =='':
            response = "CON Welcome to ida technology USSD app \n "
            response +="1. Girls in code \n"
            response +="2. Sdf program "
        else:
            response ="END "
            
        



        return HttpResponse(response)


    return HttpResponse('welcome')

