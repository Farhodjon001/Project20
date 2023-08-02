from django.shortcuts import render
from .models import Human
from django.http import JsonResponse
# Create your views here.

def get_all(request):
    if request.method=="GET":
        all_date= Human.objects.all()
        result=[]
        for human in all_date:
             result.append({"id":human.id,"human_name":human.first_name})
        return JsonResponse({"date":result})

def get_by_id(request,human_id):
    if request.method=="GET":
        try:
            date=Human.objects.get(id=human_id)
        except Human.DoesNotExists:
            return JsonResponse({"msg": "NOT FOUND"})
        return JsonResponse({"id":date.id,"pupil_name":date.first_name})