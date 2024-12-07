from django.shortcuts import render
 
def index(request):
    header = "Данные пользователя"
    langs = ['Python', "Java", "C#"]
    user = {"name": "Tom", "age": 23}
    address = ("Абрикосовая", 23, 45)
    
    data = {'header': header, "langs": langs, "user": user, "adress": address}
    return render(request, "blog/index.html", context=data)

