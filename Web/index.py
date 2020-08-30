from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return render(request, 'index.html', {'title': 'Shenzhen ShenOne Hotel Supplies Co., Ltd. ', 'message': 'Under Construction, Will Coming Out Soon!'})