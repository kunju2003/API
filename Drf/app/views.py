from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
# Create your views here.
def fun1(request):
    if request.method=='GET':
        data=student.objects.all()
        s=studSerializers(data,many=True)
        return JsonResponse(s.data,safe=False)