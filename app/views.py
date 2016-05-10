# views.py 

from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')
global num
num = []
GLOBAL_Entry = None

def test(request):
    return HttpResponse('My second view!')

def profile(request):
    return render(request, 'app/profile.html')   

def profile2(request):
    global num
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req1 = requests.get('https://api.coursera.org/api/courses.v1?q=search&query='+username+'&includes=instructorIds,partnerIds,photoUrl,partnerLogo&fields=instructorIds,partnerIds,photoUrl,partnerLogo')

        userData = []
        partnerData = []
        json_data1 = json.loads(req1.text)
        for element in json_data1['elements']:
            parsedData.append({'name':element['name'],'slug':element['slug'],'photoUrl':element['photoUrl'],'id1':element['instructorIds'][0],'pid':element['partnerIds'][0]})
        print(element['partnerIds'][0])
            

    return render(request, 'app/profile2.html', {'data': parsedData})

def profile3(request):
    parsedData = []
    if request.method == 'POST':
        id1 = request.POST.get('id1')
        pid = request.POST.get('pid')
  
       
    req2 = requests.get('https://api.coursera.org/api/instructors.v1/'+id1+'?includes=fullName,lastName&fields=fullName,lastName')
    json_data2 = json.loads(req2.text)
    print json.dumps(json_data2, indent=4, sort_keys=True)

    for element in json_data2['elements']:
        fullName = element['fullName']
        

    req2 = requests.get('https://api.coursera.org/api/partners.v1/'+pid+'?fields=name,logo&include=name,logo')
    json_data2 = json.loads(req2.text)
    print json.dumps(json_data2, indent=4, sort_keys=True)

    for element in json_data2['elements']:
        name = element['name']
        logo = element['logo']

    parsedData.append({'name':name,'logo':logo,'fullName':fullName}) 
    print json.dumps(parsedData, indent=4, sort_keys=True)
    return render(request, 'app/profile3.html', {'data': parsedData})