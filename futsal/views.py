from django.shortcuts import render


def index(request):
    return render(request, "futsal/index.html", {})


def detail(request):
    return render(request, "futsal/detail.html", {})


def about(request):
    return render(request, "futsal/about.html", {})


def contact(request):
    return render(request, "futsal/contact.html", {})