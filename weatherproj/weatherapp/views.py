from django.shortcuts import render
from django.contrib import messages
import requests
# import requests
import datetime
# Create your views here.
def index(request):
    #writing conditional for when city is added
    if 'city' in request.POST:
        city = request.POST['city']

    else:
        city = 'indore'
    #copied url with the api call and my api key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7abb17d2deb51214234624e60799314c'

    #creating parameters for temperature
    PARAMS = {'units':'metric'}

    #creating a try block in case mtu aweke vituko kwa form
    try:
        #fetching data from api
        data = requests.get(url,PARAMS).json()

        #creating variables to get the description of the weather along with the weather icon, temperature and the day
        description = data["weather"][0]['description']
        icon = data["weather"][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()
        return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occured':False})
    

    except:
        exception_occured = True
        messages.error(request,'Entered data not available to the API')
        day = datetime.date.today()

        return render(request,'index.html',{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occured':True})


    