from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest

def index(request, id):
    people = [None, "Bob", "Sam", "Tom"]
    if id in range(1, len(people)):
        return HttpResponse(people[id])
    else:
        return HttpResponseNotFound("Not Found")

def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    if (age>17):
        return HttpResponse("Доступ разрешен")
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")


