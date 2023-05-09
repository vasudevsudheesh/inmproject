from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def termsnserviece(request):
    return render(request, "termsnserviece.html")


def privacypolicy(request):
    return render(request, "privacypolicy.html")


def feedback(request):
    return render(request, "feedback.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def help(request):
    return render(request, "help.html")


def base(request):
    return render(request, "base.html")
