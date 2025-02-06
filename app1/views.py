from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
list1=[
    {"id":"1","name":"html and css", "teacher":"ahamadi","price":4000000},
    {"id":"2","name":"python", "teacher":"askari","price":6000000},
    {"id":"3","name":"c#", "teacher":"shahabi","price":5000000},
]

def search(request,name):
    l1=[]
    for item in list1:
        if name in item['name']:
            l1.append(item)
    c={'name1':l1}
    r=render(request,'new/new.html',context=c)
    return HttpResponse(r)