from django.shortcuts import render
 

def index(request):
    cat = ["Python", "Java", "JS", "GO", "C#", "Kotlin"]
    return render(request, "blog/index.html", context={"cat":cat})

